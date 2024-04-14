from ..app import db

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    imdb_id = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, title, imdb_id):
        self.title = title
        self.imdb_id = imdb_id

    def __repr__(self):
        return f'<Movie: {self.title} {self.imdb_id}>'
