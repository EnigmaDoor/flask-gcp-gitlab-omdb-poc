from typing import Optional, Dict

import requests

class OMDBException(Exception):
    def __init__(self, message: str):
        self._message = message
        super().__init__(self.message)

    @property
    def message(self) -> str:
        return self._message

class OMDB:
    """OMDB wrapper
    Args:
        apikey (str): API Key to use
        timeout (float): Timeout in seconds
    Returns:
        OMDB: OMDB wrapper
    """
    def __init__(self, apikey: str, timeout: float = 5.0):
        self.url: str = "https://www.omdbapi.com/"
        self.apikey = apikey
        self.timeout = timeout
        self._session: Optional[requests.sesion] = requests.Session()

    def close(self):
        if self._session:
            self._session.close()
            self._session = None

    def get_movie(self, title: Optional[str] = None, imdb_id: Optional[str] = None) -> Dict:
        params = {
            "apikey": self.apikey
        }
        if imdb_id:
            params['i'] = imdb_id
        elif title:
            params['t'] = title
        else:
            raise OMDBException('Either title or imdb_id is required')
        response = self._get_response(params)
        return response

    def pull_movies(self, query: str = "", amount: int = 100, page: int = 1) -> Dict:
        params = {
            "s": query,
            "page": page,
            "apikey": self.apikey,
        }
        results = []
        cont = True

        while cont and len(results) < amount:
            new_page = self._get_response(params)
            if new_page['Response'] == False:
                raise OMDBException('No response available')
            ### Append all results up to the amount specified
            results += new_page['Search'][:min(amount - len(results), len(new_page['Search']))]
            params['page'] += 1
            cont = len(results) < int(new_page['totalResults']) and len(new_page['Search']) > 0

        return results

    def _get_response(self, kwargs):
        """wrapper for the `requests` library call"""
        response = self._session.get(self.url, params=kwargs, timeout=self.timeout).json()
        return response
