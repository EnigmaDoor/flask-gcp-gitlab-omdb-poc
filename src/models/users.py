from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import Column, Integer, String
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True, nullable=False)
    password_hashed = Column(String(255), nullable=False)

    def __init__(self, email, password_plaintext):
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)

    def set_password(self, password_plaintext: str):
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)

    def __repr__(self):
        return f'<User: {self.email}>'
