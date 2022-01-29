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

vinted = Vinted("fr")

# search(url, number_of_items, page_number)
vinted.search("https://www.vinted.fr/vetement?order=newest_first&price_to=60&currency=EUR",10,1)

```