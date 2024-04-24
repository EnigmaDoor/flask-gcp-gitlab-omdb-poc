"""
11;rgb:3030/0a0a/2424Movie entity specific service
"""
from flask import abort
from src.services.base import BaseService
from src.repositories.movies import MoviesRepository
from src.models.movies import Movie
from src.app import app
from src.omdb import OMDB

class MoviesService(BaseService):
    def __init__(self):
        BaseService.__init__(self, MoviesRepository)
        self.omdb = OMDB(app.config['OMDB_APIKEY'])

    def create_from_imdb(self, title, imdb_id):
        imdb_movie = self.omdb.get_movie(title, imdb_id)
        if 'Title' not in imdb_movie or 'imdbID' not in imdb_movie:
            raise HTTPException(404, 'Not found in IMDB')
        movie = Movie(
            title=imdb_movie.get('Title'),
            imdb_id=imdb_movie.get('imdbID'),
            year=imdb_movie.get('Year'),
            poster=imdb_movie.get('Poster'),
            type=imdb_movie.get('Type'),
        )
        movie = self.repository.create(movie)
        movie = self.repository.get(movie.id)
        return movie
