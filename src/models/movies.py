from typing import Optional
from sqlalchemy import Column, Integer, String
from .base import BaseModel

class Movie(BaseModel):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=False, nullable=False)
    imdb_id = Column(String(128), unique=True, nullable=False)
    year = Column(String(32), unique=False, nullable=True)
    type = Column(String(32), unique=False, nullable=True)
    poster = Column(String(256), unique=False, nullable=True)

    def __init__(self, title: str, imdb_id: str, year: Optional[str]=None, type: Optional[str]=None, poster: Optional[str]=None):
        self.title = title
        self.imdb_id = imdb_id
        self.year = year
        self.type = type
        self.poster = poster

    def __repr__(self):
        return f'<Movie {self.id}: {self.title} {self.imdb_id}>'
