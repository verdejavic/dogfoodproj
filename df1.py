from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = "http://slimdoggy.com/dogfood/dry/acana-adult-large-breed/"

# open a page and get all html on that page - return bsObj



# get data from each detail page and write it to a csv file
def get_food_details():
    def open_page(site):
        req = Request(site, headers=hdr)
        try:
            html = urlopen(req)
        except HTTPError as e:
            print(e.reason)
        except:
            print("Unknown error")
        bsObj = BeautifulSoup(html, "html.parser")
        return bsObj
    bsObj = open_page(site)    
    name = (bsObj.find("h1")[1])
    print(name.get_text())

    #html = urlopen("http://slimdoggy.com/dogfood/dry/acana-adult-large-breed/")
    #bsObj = BeautifulSoup(html, 'html.parser')
