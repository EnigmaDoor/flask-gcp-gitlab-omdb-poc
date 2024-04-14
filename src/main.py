import os

from .omdb import OMDB
from .app import app
from .models import Movie, User

def main(mode: str = 'ONLINE'):
    # If no DB content, pull movies
    if mode == 'ONLINE':
        omdb = OMDB(app.config['OMDB_APIKEY'])
        results = omdb.pull_movies('test', 10) # put amount back to 100
        print("===>", results, "\n", len(results))
        # Load in DB
