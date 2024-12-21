from datetime import datetime, timezone
from pyVinted.requester import requester
from urllib.parse import urlparse
from pyVinted.settings import Urls

class Item:
    def __init__(self, data):
        self.raw_data = data
        self.id = data["id"]
        self.title = data["title"]
        self.brand_title = data["brand_title"]
        try:
            self.size_title = data["size_title"]
        except:
            self.size_title = data["size_title"]
        self.currency = data["price"]["currency_code"]
        self.price = data["price"]["amount"]
        self.photo = data["photo"]["url"]
        self.url = data["url"]
        self.created_at_ts = datetime.fromtimestamp(
            data["photo"]["high_resolution"]["timestamp"], tz=timezone.utc
        )
        self.raw_timestamp = data["photo"]["high_resolution"]["timestamp"]

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(('id', self.id))

    def isNewItem(self, minutes=3):
        delta = datetime.now(timezone.utc) - self.created_at_ts
        return delta.total_seconds() < minutes * 60

    def getDescription(self, translated=True):
        locale = urlparse(self.url).netloc
        requester.setLocale(locale)
        try:
            response = requester.get(url=f"https://{locale}{Urls.VINTED_API_URL}/items/{self.id}/plugins/translatable?localize={translated}")
            response = response.json()
            return response["plugins"][1]["data"]["description"]
        except:
            return None

    def getPhotos(self):
        locale = urlparse(self.url).netloc
        requester.setLocale(locale)
        try:
            response = requester.get(url=f"https://{locale}{Urls.VINTED_API_URL}/items/{self.id}")
            response = response.json()
            urls = set()
            for photo in response["item"]["photos"]:
                urls.add(photo["full_size_url"])
            return urls
        except:
            return None
