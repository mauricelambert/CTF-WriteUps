from app.utils.auth import init_db
from flask import Flask
from app.blueprints.routes import server 

app = Flask(__name__)

init_db()
app.register_blueprint(server)
