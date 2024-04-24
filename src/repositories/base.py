"""
Holds shared implementation of all repositories.
"""
from src.models import db

class BaseRepository(object):
    def __init__(self, model):
        """
        Initialize the repository object
        :param model: e.g. Users
        """
        self.model = model

    def get(self, entity_id):
        entity = db.session.get(self.model, entity_id)
        return entity

    def get_all(self):
        query = db.session.query(self.model).all()
        return entities

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()

    def update(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
