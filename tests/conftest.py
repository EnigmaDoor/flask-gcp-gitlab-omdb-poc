import os
import pytest
from src.app import create_app, setup_app
from src.models import User, Movie

from src.services.movies import MoviesService

# -------- # Fixtures # --------
@pytest.fixture(scope='session')
def test_app():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    test_app = create_app()
    setup_app(test_app)
    yield test_app

@pytest.fixture(scope='session')
def test_client(test_app):
    return test_app.test_client()

@pytest.fixture(scope='module')
def new_user():
    user = User('admin@admin.admin', 'admin')
    return user

@pytest.fixture(scope='module')
def new_movie():
    movie = Movie(title='Testing movie', imdb_id='imdbID')
    return movie

@pytest.fixture(scope='module')
def new_movies_in_db(test_app):
    with test_app.app_context():
        movies_service = MoviesService()
        movies = [
            movies_service.create(Movie(title='TestingMovie1', imdb_id='imdbID1')),
            movies_service.create(Movie(title='TestingMovie2', imdb_id='imdbID2')),
            movies_service.create(Movie(title='TestingMovie3', imdb_id='imdbID3')),
            movies_service.create(Movie(title='TestingMovie4CUSTOM', imdb_id='imdbID4')),
        ]
        yield movies
        # yield is required, otherwise the movies' session is expired during test_app
