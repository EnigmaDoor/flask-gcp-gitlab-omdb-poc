"""
Movie entity specific service
"""
from src.services.base import BaseService
from src.repositories.movies import MoviesRepository

class MoviesService(BaseService):
    def __init__(self):
        BaseService.__init__(self, MoviesRepository)
