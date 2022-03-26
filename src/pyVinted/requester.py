import json
import requests
import re
from requests.exceptions import HTTPError


class Requester:
    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
            "sec-fetch-dest": "none",
            "accept": "*/*",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "accept-language": "en-US",
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

        data = json.loads(response.content)

        return data

    # def post(self, url, params=None):
    #     """
    #     Perform a http post request.
    #     :param url: str
    #     :param params: dict, optional
    #     :return: dict
    #         Json format
    #     """
    #     response = self.session.post(url, headers=self.headers, params=params)
    #     if response.status_code != 200:
    #         raise HTTPError
    #     if not response.content:
    #         return None
    #     data = json.loads(response.content)

    #     return data

    def setCookies(self, domain):
        """used to set cookies"""
        self.VINTED_URL = f"https://www.vinted.{domain}"
        self.VINTED_API_URL = f"https://www.vinted.{domain}/api/v2"
        self.VINTED_PRODUCTS_ENDPOINT = "catalog/items"

        #regex to find _vinted_*** in set-cookie header
        p = re.compile('(?=_vinted_)(.*?);')


        try:
            response = self.session.get(self.VINTED_URL)
            response.raise_for_status()

            cookies = response.headers["set-cookie"]

            #creating vinted_session cookie
            vinted_session = p.search(cookies).group()
            vinted_session = vinted_session.replace(";", "")
            vinted_session = vinted_session.split("=")
            vinted_session = {vinted_session[0]: vinted_session[1]}

            #retrieving old cookies from session
            old_cookies = self.session.cookies.get_dict()

            new_cookies = dict(vinted_session, **old_cookies)

            self.session.cookies.update(new_cookies)

            print("Cookies set!")

        except Exception as e:
            print(
                f"There was an error fetching cookies for {self.VINTED_URL}\n Error : {e}"
            )

    # def login(self,username,password=None):

    #     # client.headers["X-Csrf-Token"] = csrf_token
    #     # client.headers["Content-Type"] = "*/*"
    #     # client.headers["Host"] = "www.vinted.fr"
    #     print(self.session.headers)
    #     urlCaptcha = "https://www.vinted.fr/api/v2/captchas"
    #     dataCaptcha = {"entity_type":"login", "payload":{"username": username }}

    #     token_endpoint  = "https://www.vinted.fr/oauth/token"
    #     uuid = self.session.post(urlCaptcha, data=json.dumps(dataCaptcha)).json()["uuid"]
    #     log = {"client_id":"web","scope":"user","username":username,"password":password,"uuid":uuid,"grant_type":"password"}
    #     b = self.session.post(token_endpoint, data=json.dumps(log) )
    #     print(b.text)

    # def message(self):
    #     response = self.session.get("https://www.vinted.fr/api/v2/users/33003526/msg_threads?page=1&per_page=20")
    #     print(response.text)


requester = Requester()
