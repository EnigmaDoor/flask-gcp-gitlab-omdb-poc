import os
from flask.cli import FlaskGroup
from src.app import app, db
from src.config import Config
from src.omdb import OMDB
from src.models import Movie, User

app.config.from_object(Config)

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    omdb = OMDB(app.config['OMDB_APIKEY'])
    movies_set = omdb.pull_movies('test', app.config['OMDB_TOSEED'])
    movies = map(lambda x: Movie(title=x['Title'], imdb_id=x['imdbID']), movies_set)
    for movie in movies:
        db.session.add(movie)
    db.session.add(User(email='admin@admin.admin', password_plaintext='admin'))
    db.session.commit()

if __name__ == '__main__':
    cli()
