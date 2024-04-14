"""
Users entity specific repository
"""
from src.models.users import User
from src.repositories.base import BaseRepository

class UsersRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, User)
