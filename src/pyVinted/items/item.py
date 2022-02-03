from datetime import datetime, timezone

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
    
    def isNewItem(self, delay=3):
        delta = datetime.now(timezone.utc) - self.updated_at_ts
        return delta.seconds < delay*60