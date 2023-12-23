from config import upload as upload_dir
from functools import wraps
from flask import Blueprint, send_from_directory, render_template_string, render_template, request, redirect, make_response, send_file, abort
import os
from app.utils.auth import user_registered, verify_token
from fileinput import filename

server = Blueprint("server", __name__)

def auth_middleware(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("token")
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            current_user = verify_token(token)
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated

@server.route("/", methods=["GET"])
def index():
    return render_template("home.html")

@server.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@server.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    if not username or not password:
        return render_template('home.html'), 400

    token = user_registered(username, password) 
    
    if not token:
        return render_template('home.html'), 400

    response = make_response(redirect("/")) 
    response.set_cookie("token", token, samesite='Strict', httponly=True)
    return response


@server.route("/files", methods=["GET"])
@auth_middleware
def get_file():
    file = request.args.get('f')
    
    if not file: 
        response = make_response(redirect("/home?error=parameter f not set")) 
        return response

    if file:
        if "./" in file or "../" in file or "%" in file:
            return render_template_string("No LFI here :)")
        return send_from_directory(upload_dir, file)

@server.route("/upload", methods=["GET", "POST"])
@auth_middleware
def upload():
    if request.method == "GET":
        return render_template('upload.html'), 200
    if request.method == "POST":
        f = request.files['file']
        if not f:
            return render_template('home.html'), 400

        f.save(upload_dir+f.filename)
        return render_template_string(f"You uploaded : {f.filename}")
    return render_template('home.html'), 400
