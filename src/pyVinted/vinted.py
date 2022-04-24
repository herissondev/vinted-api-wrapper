from urllib.parse import urlparse, parse_qsl
import requests
from .items.item import Item
from pyVinted.items import Items
from pyVinted.requester import requester


class Vinted:
    """
    This class is built to connect with the pyVinted API.

    It's main goal is to be able to retrieve items from a given url search.\n
    The items are then returned in a json format
    """

    def __init__(self, domain="fr", proxy=None, gateway=None):
        """
        Args:
            domain (str): Domain to be used, example: "fr" for France, "de" for Germany...

        """

        if proxy is not None:
            requester.session.proxies.update(proxy)

        elif gateway is not None:
            requester.setCookies(domain=domain,gateway=gateway)
            #requester.session.mount("https://www.vinted.fr", gateway)
        else:
            requester.setCookies(domain=domain)


        self.items = Items()


