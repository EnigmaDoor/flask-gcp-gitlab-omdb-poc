"""
Movies entity specific repository
"""
from src.models.movies import Movie
from src.repositories.base import BaseRepository

class MoviesRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Movie)
