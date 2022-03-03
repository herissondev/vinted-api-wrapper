from urllib.parse import urlparse,parse_qsl
import requests
from .items.item import Item
from pyVinted.items import Items
from pyVinted.requester import requester

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
        requester.setCookies(domain)
        self.items = Items()
    
    # def login(self,username,password):
    #     requester.login(username=username, password=password)
    #     requester.message()
        

    

    
        

    

    


    
        
    