import os
import pytest
from src.app import create_app
from src.models import User, Movie

# -------- # Fixtures # --------
@pytest.fixture(scope='module')
def test_app():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    test_app, test_db = create_app()
    yield test_app

@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()

@pytest.fixture(scope='module')
def new_user():
    user = User('admin@admin.admin', 'admin')
    return user

@pytest.fixture(scope='module')
def new_movie():
    movie = Movie('Testing movie', 'imdbID')
    return movie
