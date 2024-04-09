from flask import Blueprint

indexRoutes = Blueprint('index', __name__)

@routes.route('/hello')
def hello():
    return "Hello World"
