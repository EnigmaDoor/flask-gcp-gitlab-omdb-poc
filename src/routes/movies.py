"""
Handles Person APIs
Performs request and response serialization and deserialization respectively
For business logic implementation; it relies on service layer.
"""
import logging
from flask import Blueprint, request
from .utils import json_response, json_error_response
from src.models import Movie
from src.services.movies import MoviesService

moviesRoutes = Blueprint('movies', __name__)
movies_service = MoviesService()

@moviesRoutes.route('/<movie_id>', methods=["GET"])
def get_one(movie_id):
    try:
        movie = movies_service.get(movie_id)
        result = movie.serialize
        return json_response(result)
    except Exception as e:
        return json_error_response(e)

@moviesRoutes.route('/', strict_slashes=False)
def get_all():
    try:
        page = request.args.get('page', default=1, type=int)
        quantity = request.args.get('quantity', default=10, type=int)
        filters = request.args.get('filters', default = '', type = str)

        movies = movies_service.get_all(page, quantity, filters)
        result = [movie.serialize for movie in movies]
        return json_response(result)
    except Exception as e:
        return json_error_response(e)

@moviesRoutes.route('/', methods=["POST"], strict_slashes=False)
def create_from_imdb():
    form_dict = request.get_json()
    try:
        movie = movies_service.create_from_imdb(form_dict.get('title'), form_dict.get('imdb_id'))
        return json_response(movie.serialize)
    except Exception as e:
        return json_error_response(e)

@moviesRoutes.route('/<movie_id>', methods=["DELETE"])
def delete(movie_id):
    try:
        movies_service.delete(movie_id)
        return json_response('Deleted')
    except Exception as e:
        return json_error_response(e)
