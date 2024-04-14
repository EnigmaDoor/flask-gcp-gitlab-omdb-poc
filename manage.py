import os
from flask.cli import FlaskGroup

from src.app import app, db
from src.config import Config

app.config.from_object(Config)

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()
