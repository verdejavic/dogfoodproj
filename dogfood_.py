from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = "http://slimdoggy.com/dogfood/?searchtype=basic&foodtype=All&foodbrand=All&foodranking=All&brandrecipesearch=&ingredientsin=&ingredientsout=propylene+glycol+AND+ethoxyquin+AND+BHA+AND+BHT+AND+TBHQ+AND+propyl+gallate"

def open_page(site):
    req = Request(site, headers=hdr)
    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e.reason)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj

bsObj = open_page(site)
p = open("food_urls.txt", "w")
urls_list = []

def get_next_page(html, bsObj):
    for i in range (1, 32):
        new_url = "http://slimdoggy.com/dogfood/page/" + str(i) + "/?searchtype=basic&foodtype=All&foodbrand=All&foodranking=All&brandrecipesearch&ingredientsin&ingredientsout=propylene%20glycol%20AND%20ethoxyquin%20AND%20BHA%20AND%20BHT%20AND%20TBHQ%20AND%20propyl%20gallate"
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        get_urls(html,bsObj)

# THIS WORKS - writes all URLs to the file
def get_urls(bsObj):
    # get 3rd table
    table = bsObj.findAll("table")[2]
    # get all td elements from table
    a_list = table.findAll("a")
    for link in a_list:
        if 'href' in link.attrs:
            # urls_list.append(str(link.attrs['href']))
            p.write(str(link.attrs['href']) + "\n")
    for i in range (1, 32):
        new_url = "http://slimdoggy.com/dogfood/page/" + str(i) + "/?searchtype=basic&foodtype=All&foodbrand=All&foodranking=All&brandrecipesearch&ingredientsin&ingredientsout=propylene%20glycol%20AND%20ethoxyquin%20AND%20BHA%20AND%20BHT%20AND%20TBHQ%20AND%20propyl%20gallate"
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        get_next_page(html, bsObj)



get_urls(bsObj)
# get_food_details(food_list)
p.close()
