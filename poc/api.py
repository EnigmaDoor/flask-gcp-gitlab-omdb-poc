from flask import Flask
from routes import *

def setup_flask():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app
