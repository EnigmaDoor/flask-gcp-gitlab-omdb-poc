"""
Handles Person APIs
Performs request and response serialization and deserialization respectively
For business logic implementation; it relies on service layer.
"""
from flask import Blueprint, request
from .utils import json_response, json_error_response
from src.models import Movie
from src.services.movies import MoviesService

moviesRoutes = Blueprint('movies', __name__)
movies_service = MoviesService()

@moviesRoutes.route('/<movie_id>')
def get_one(movie_id):
    try:
        movie = movies_service.get(movie_id)
        result = movie.serialize
        return json_response(result)
    except Exception as e:
        return json_error_response(e)

@moviesRoutes.route('/')
def get_all():
    try:
        movies = movies_service.get_all()
        result = [movie.serialize for movie in movies]
        return json_response(result)
    except Exception as e:
        return json_error_response(e)
