"""
User entity specific service
"""
from src.services.base import BaseService
from src.repositories.users import UsersRepository

class UsersService(BaseService):
    def __init__(self):
        BaseService.__init__(self, UsersRepository)
