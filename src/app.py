import os
import logging
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

    # Setup DB
    db.init_app(app)

    # Setup logging
    if not app.debug:
        logging.getLogger(app.name).addHandler(logging.StreamHandler())
        logging.getLogger(app.name).setLevel(logging.INFO)
    logging.basicConfig(format=app.config.get('LOG_FORMAT'))
    logging.getLogger().setLevel(app.config.get('LOG_LEVEL'))

    # App built
    return app

def setup_app(app):
    setup_routes(app)

app = create_app()
setup_app(app)
