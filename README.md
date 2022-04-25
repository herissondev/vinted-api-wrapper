# Vinted-Api-Wrapper
Simple python package that uses the Vinted API to search new posts.

## Install
Simpely install package using pip :
```
pip install pyVinted
```
## Example

```py
from pyVinted import Vinted

vinted = Vinted()

# search(url, number_of_items, page_number)
items = vinted.items.search("https://www.vinted.fr/vetement?order=newest_first&price_to=60&currency=EUR",10,1)
#returns a list of objects: item

```
You can access Item attributes as shown here:
```py
item1 = items[0]
#title
item1.title
#id
item1.id
#photo url
item1.photo
#brand
item1.brand_title
#price
item1.price
#url
item1.url
#currency
item1.currency
```

