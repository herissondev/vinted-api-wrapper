from urllib.parse import urlparse,parse_qsl
import requests


class Vinted:
    '''
    This class is built to connect with the pyVinted API.

    It's main goal is to be able to retrieve items from a given url search.\n
    The items are then be returned in a json format
    '''

    def __init__(self, domain = "fr"):
        """
        Args:
            domain (str): Domain to be used, example: "fr" for France, "de" for Germany...
            
        """
        
        self.VINTED_URL = f'https://www.vinted.{domain}'
        self.VINTED_API_URL = f'https://www.vinted.{domain}/api/v2'
        self.VINTED_PRODUCTS_ENDPOINT = 'items'

        self.session = requests.Session()
        self.setCookies()


    def parseUrl(self, url, nbrItems=20, page=1):
        '''
        Parse Vinted search url to get parameters the for api call.
        
        Args:
            url (str): The url of the research on vinted.
            nbrItems (int): Number of items to be returned (default 20).
            page (int): Page number to be returned (default 1).
            
        '''
        querys = parse_qsl(urlparse(url).query)
        params = {

                    'search_text': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'search_text'])),
                    'catalog_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'catalog[]'])) ,
                    'color_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'color_id[]'])) ,
                    'brand_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'brand_id[]'])) ,
                    'size_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'size_id[]'])) ,
                    'material_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'material_id[]'])) ,
                    'status_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'status[]'])) ,
                    'country_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'country_id[]'])) ,
                    'city_ids': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'city_id[]'])) ,
                    'is_for_swap': ','.join(map(str, [1 for tpl in querys if tpl[0] == 'disposal[]'])),
                    'currency': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'currency'])),
                    'price_to': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'price_to'])),
                    'price_from': ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'price_from'])),
                    'page': page,
                    'per_page': nbrItems,
                    "order": ','.join(map(str, [tpl[1] for tpl in querys if tpl[0] == 'order']))
        }
        
        return params
        

    def search(self,url,nbrItems=20, page=1):
        '''
        Retrieves items from a given search url on vited.
        
        Args:
            url (str): The url of the research on vinted.
            nbrItems (int): Number of items to be returned (default 20).
            page (int): Page number to be returned (default 1).
            
        '''
        try:
            params = self.parseUrl(url,nbrItems,page)
            url = f'{self.VINTED_API_URL}/{self.VINTED_PRODUCTS_ENDPOINT}'
            response = self.session.get(url=url, params=params)
            
            response.raise_for_status()
            items = response.json()["items"]
            return items

        except Exception as e:
            print(f"Error : {e}")


    def setCookies(self):
        print(f"Getting cookies from {self.VINTED_URL}")
        try :
            response = self.session.get(self.VINTED_URL)
            cookies = self.session.cookies.get_dict()
            headers = dict({"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"}, **cookies)
            self.session.headers.update(headers)
            response.raise_for_status()
            print("Cookies set!")

        except Exception as e:
            print(f"There was an error fetching cookies for {self.VINTED_URL}\n Error : {e}")
        