import json
import requests
import re
import random
from requests.exceptions import HTTPError


class Requester:

    def __init__(self):

        self.HEADER = {
            "User-Agent": "PostmanRuntime/7.28.4",  # random.choice(USER_AGENTS),
            "Host": "www.vinted.fr",
        }
        self.VINTED_AUTH_URL = "https://www.vinted.fr/"
        self.MAX_RETRIES = 3
        self.session = requests.Session()
        self.session.headers.update(self.HEADER)
        # self.setCookies()

    def setLocale(self, locale):
        """
            Set the locale of the requester.
            :param locale: str
        """
        self.VINTED_AUTH_URL = f"https://{locale}/"
        self.HEADER = {
            "User-Agent": "PostmanRuntime/7.28.4",  # random.choice(USER_AGENTS),
            "Host": f"{locale}",
        }
        self.session.headers.update(self.HEADER)

    def get(self, url, params=None):
        """
        Perform a http get request.
        :param url: str
        :param params: dict, optional
        :return: dict
            Json format
        """
        tried = 0
        while tried < self.MAX_RETRIES:
            tried += 1
            with self.session.get(url, params=params) as response:

                if response.status_code == 401 and tried < self.MAX_RETRIES:
                    print(f"Cookies invalid retrying {tried}/{self.MAX_RETRIES}")
                    self.setCookies()

                elif response.status_code == 200 or tried == self.MAX_RETRIES:
                    return response

        return HTTPError

    def post(self, url, params=None):
        response = self.session.post(url, params)
        response.raise_for_status()
        return response

    def setCookies(self):

        self.session.cookies.clear_session_cookies()

        try:

            self.session.head(self.VINTED_AUTH_URL)
            print("Cookies set!")

        except Exception as e:
            print(
                f"There was an error fetching cookies for vinted\n Error : {e}"
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
