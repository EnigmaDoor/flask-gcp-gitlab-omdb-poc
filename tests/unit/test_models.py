from src.models import Movie, User

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    assert new_user.email == 'admin@admin.admin'
    assert new_user.password_hashed != 'admin'

def test_new_movie(new_movie):
    """
    GIVEN a Movie model
    WHEN a new Movie is created
    THEN check the fields are defined correctly
    """
    assert new_movie.title == 'Testing movie'
    assert new_movie.imdb_id == 'imdbID'
