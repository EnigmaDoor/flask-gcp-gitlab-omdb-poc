import os
from flask import Flask
from dotenv import load_dotenv

from .config import Config
from .db import setup_db
from .routes import setup_routes

# Load environment
load_dotenv()

# Setup Flask
app = Flask(__name__)
app.config.from_object(Config)
setup_routes(app)

# Load & check DB content
db = setup_db(app)

print("INITIALIZED APP")
