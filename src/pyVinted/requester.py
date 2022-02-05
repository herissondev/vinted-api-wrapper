import json
import requests
from requests.exceptions import HTTPError


class Requester:

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'sec-fetch-dest': 'none',
            'accept': '*/*',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'accept-language': 'en-US'
        }

        

        self.session = requests.Session()

    def get(self, url, params=None):
        """
        Perform a http get request.
        :param url: str
        :param params: dict, optional
        :return: dict
            Json format
        """
        response = self.session.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise HTTPError
        if not response.content:
            return None
        data = json.loads(response.content)
        
        return data

    def setCookies(self, domain):

        self.VINTED_URL = f'https://www.vinted.{domain}'
        self.VINTED_API_URL = f'https://www.vinted.{domain}/api/v2'
        self.VINTED_PRODUCTS_ENDPOINT = 'items'

        print(f"Getting cookies from {self.VINTED_URL}")
        try :
            response = self.session.get(self.VINTED_URL)
            response.raise_for_status()
            cookies = self.session.cookies.get_dict()
            headers = dict({"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"}, **cookies)
            self.session.headers.update(headers)
            print("Cookies set!")

        except Exception as e:
            print(f"There was an error fetching cookies for {self.VINTED_URL}\n Error : {e}")


requester = Requester()