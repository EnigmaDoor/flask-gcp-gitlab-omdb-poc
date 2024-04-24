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
    seed_from_omdb = app.config['OMDB_USE_TO_SEED']
    if seed_from_omdb:
        omdb = OMDB(app.config['OMDB_APIKEY'])
        movies_set = omdb.pull_movies('test', app.config['OMDB_TOSEED'])
        print("ADDING", movies_set)
        movies = map(lambda x: Movie(
            title=x['Title'], imdb_id=x['imdbID'],
            year=x['Year'], type=x['Type'],
            poster=x['Poster'],
        ), movies_set)
        for movie in movies:
            db.session.add(movie)
    else:
        db.session.add(Movie(title='movie seed 1', imdb_id='1'))
        db.session.add(Movie(title='movie seed 2', imdb_id='2'))
        db.session.add(Movie(title='movie seed 3', imdb_id='3'))
    db.session.add(User(email='admin@admin.admin', password_plaintext='admin'))
    db.session.commit()

if __name__ == '__main__':
    cli()
