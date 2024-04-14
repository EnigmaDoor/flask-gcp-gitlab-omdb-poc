from flask import Blueprint

indexRoutes = Blueprint('index', __name__)

@indexRoutes.route('/hello')
def hello():
    return "Hello World"
