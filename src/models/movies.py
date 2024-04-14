from sqlalchemy import Column, Integer, String
from .base import BaseModel

class Movie(BaseModel):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=False, nullable=False)
    imdb_id = Column(String(128), unique=True, nullable=False)

    def __init__(self, title, imdb_id):
        self.title = title
        self.imdb_id = imdb_id

    def __repr__(self):
        return f'<Movie: {self.title} {self.imdb_id}>'
