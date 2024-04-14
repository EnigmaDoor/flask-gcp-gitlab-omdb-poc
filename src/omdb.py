from typing import Optional, Dict

import requests

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
                print(new_page)
                return results
            ### Append all results up to the amount specified
            results += new_page['Search'][:min(amount - len(results), len(new_page['Search']))]
            params['page'] += 1
            cont = len(results) < int(new_page['totalResults']) and len(new_page['Search']) > 0

        return results

    def _get_response(self, kwargs):
        """wrapper for the `requests` library call"""
        response = self._session.get(self.url, params=kwargs, timeout=self.timeout).json()
        return response
