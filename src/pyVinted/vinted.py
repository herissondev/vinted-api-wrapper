from urllib.parse import urlparse, parse_qsl
import requests
from .items.item import Item
from pyVinted.items import Items
from pyVinted.requester import requester


class Vinted:
    """
    This class is built to connect with the pyVinted API.

    It's main goal is to be able to retrieve items from a given url search.\n
    The items are then be returned in a json format
    """

    def __init__(self, domain="fr", proxy=None, gateway=None):
        """
        Args:
            domain (str): Domain to be used, example: "fr" for France, "de" for Germany...

        """
        if proxy is not None:
            requester.session.proxies.update(proxy)

        if gateway is not None:
            requester.session.mount("https://www.vinted.fr", gateway)

        requester.setCookies(domain)
        self.items = Items()

    # def login(self,username,password):
    #     requester.login(username=username, password=password)
    #     requester.message()
