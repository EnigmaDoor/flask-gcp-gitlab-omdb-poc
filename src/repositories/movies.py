"""
Movies entity specific repository
"""
from src.models import db
from src.models.movies import Movie
from src.repositories.base import BaseRepository

class MoviesRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Movie)

    def get_all(self, page: int=1, quantity: int=10, filters: str=''):
        entities = db.session.query(Movie)
        if len(filters):
            entities = entities.filter(Movie.title.contains(filters))
        entities = entities.order_by(Movie.title.asc()).paginate(page=page, per_page=quantity)
        return entities
