from datetime import datetime, timezone
from pyVinted.requester import requester
 
class Item:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.size = data['size']
        self.brand = data['brand']
        self.currency = data['currency']
        self.price_numeric = data['price_numeric']
        self.created_at_ts = datetime.fromisoformat(data['created_at_ts'])
        self.updated_at_ts = datetime.fromisoformat(data['updated_at_ts'])
        self.photos = [ photo['full_size_url'] for photo in data['photos']]
        self.city = data['city']
        self.country = data['country']
        self.status_id = data['status_id']
        self.url = f"{requester.VINTED_URL}{data['path']}"
    
    def isNewItem(self, minutes=3):
        delta = datetime.now(timezone.utc) - self.created_at_ts
        return delta.seconds < minutes*60