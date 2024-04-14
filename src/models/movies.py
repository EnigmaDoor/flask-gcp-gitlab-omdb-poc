from ..app import db

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    omdb_id = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, title, omdb_id):
        self.title = title
        self.omdb_id = omdb_id
