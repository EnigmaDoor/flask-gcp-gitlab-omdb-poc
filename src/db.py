import os
from flask_sqlalchemy import SQLAlchemy

def setup_db(app):
    db = SQLAlchemy(app)
    return db
