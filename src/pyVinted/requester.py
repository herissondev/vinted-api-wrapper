import json
import requests
import re
import random
from requests.exceptions import HTTPError



HEADERS = {
            "User-Agent": "PostmanRuntime/7.28.4",  # random.choice(USER_AGENTS),
            "Host": "www.vinted.fr",
}
class Requester:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)



    def get(self, url, params=None):
        """
        Perform a http get request.
        :param url: str
        :param params: dict, optional
        :return: dict
            Json format
        """
        response = self.session.get(url, params=params)

        response.raise_for_status()

        return response.json()

    def post(self,url, params=None):
        response = self.session.post(url, params)
        response.raise_for_status()
        return response

    def setCookies(self, domain="fr"):
        """used to set cookies"""
        self.VINTED_URL = f"https://www.vinted.{domain}"
        self.VINTED_AUTH_URL = f"https://www.vinted.{domain}/auth/token_refresh"
        self.VINTED_API_URL = f"https://www.vinted.{domain}/api/v2"
        self.VINTED_PRODUCTS_ENDPOINT = "catalog/items"


        try:
            self.post(self.VINTED_AUTH_URL)
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
