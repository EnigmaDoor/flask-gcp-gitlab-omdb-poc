import os
from flask import Flask
from dotenv import load_dotenv

from .config import Config
from .models import db
from .routes import setup_routes

def create_app():
    # Load environment
    load_dotenv()

    # Setup Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    setup_routes(app)

    # Setup DB
    db.init_app(app)

    return app

app = create_app()
