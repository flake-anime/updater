import requests
import random
from bs4 import BeautifulSoup
from urllib3 import proxy_from_url

class FreeProxyListWrapper:
    def __init__(self):
        self.proxy_list = None
        self.get_proxy_list()

    def get_proxy_list(self):
        if not self.proxy_list == None:
            return self.proxy_list

        page = requests.get("https://free-proxy-list.net/")
        soup = BeautifulSoup(page.content, 'html.parser')
        self.proxy_list = soup.select_one("textarea").get_text().split("\n")[3:-1]

        return self.proxy_list
    
    def get_random_proxy(self):
        random_proxy = random.choice(self.proxy_list)
        return random_proxy