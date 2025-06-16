from flask import Flask
from config import UPLOAD_FOLDER
import os

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    # config
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from app.routes import main
    app.register_blueprint(main)

    return app
