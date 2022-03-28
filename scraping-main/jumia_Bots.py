import requests
import os
from bs4 import BeautifulSoup  
class JumiaBot:
    def __init__(self):
        pass
    def get_product_title(self,soup):
        return soup.find('h1',{'class':'-fs20 -pts -pbxs'}).get_text().strip()
    def get_product_data(self, product_url):
        r=requests.get(product_url)
        if r.status_code==200:  
           #print(r.content)
            soup=BeautifulSoup(r.content, 'html.parser')
            title=get_product_title(soup)
        return {
                "url":product_url,
                "title":title
            }