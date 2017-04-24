from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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
f = open("food_urls.txt", "w")

#get 3rd table
table = bsObj.findAll("table")[2]
#get all td elements from table
a_list = table.findAll("a")

for link in a_list:
    if 'href' in link.attrs:
        f.write(str(link.attrs['href']) + "\n")
    else:
        f.write("no href")

f.close()
