__author__ = 'Jack'
import requests
from lxml import html


def get_picture(URL):
    if(URL is not None):
        allNames = requests.get(URL)
        #print(allNames.text)
        tree = html.fromstring(allNames.text)

        #get the pic
        celeb_elements = tree.xpath('//img[@id = "name-poster"]/@src')
        return celeb_elements
    else:
        return None

