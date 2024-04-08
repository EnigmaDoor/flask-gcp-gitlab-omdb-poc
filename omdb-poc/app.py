import os
from dotenv import load_dotenv
from omdb import OMDB
from api import setup_flask

def main():
    # Load environment
    load_dotenv()
    apikey = os.getenv('OMDB_APIKEY')

    # Load & check DB content


    # If no DB content, pull movies
    if True:
        omdb = OMDB(apikey)
        results = omdb.pull_movies("test", 10) # put amount back to 100
        print("===>", results, "\n", len(results))
        # Load in DB

    # Run Flask
    app = setup_flask()
    app.run(host='0.0.0.0', port=os.getenv['PORT'])
