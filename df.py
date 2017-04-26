from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# first URL complete
site = "http://slimdoggy.com/dogfood/?searchtype=basic&foodtype=All&foodbrand=All&foodranking=All&brandrecipesearch=&ingredientsin=&ingredientsout=propylene+glycol+AND+ethoxyquin+AND+BHA+AND+BHT+AND+TBHQ+AND+propyl+gallate"

# front part of all other URLs
start = "http://slimdoggy.com/dogfood/page/"

# last part of all other URLs
end = "/?searchtype=basic&foodtype=All&foodbrand=All&foodranking=All&brandrecipesearch&ingredientsin&ingredientsout=propylene%20glycol%20AND%20ethoxyquin%20AND%20BHA%20AND%20BHT%20AND%20TBHQ%20AND%20propyl%20gallate"


# open a page and get all html on that page - return bsObj
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

# write all URLs from one list page to the file, p
def get_urls(bsObj):
    # get 3rd table
    table = bsObj.findAll("table")[2]
    # get all td elements from table
    a_list = table.findAll("a")
    for link in a_list:
        if 'href' in link.attrs:
            # urls_list.append(str(link.attrs['href']))
            p.write(str(link.attrs['href']) + "\n")

# get data from each detail page and write it to a csv file
def get_food_details():
    pass

# cycle through all pages that list the URLs
def get_all_urls(site, start, end):
    # start at 2, end at 31 - don't worry, it gets the first page too
    for i in range (2, 32):
        # get html from list page
        bsObj = open_page(site)
        # get all URLs from list page
        get_urls(bsObj)
        # change value of site to the _next_ URL
        site = start + str(i) + end
        # a message for you in Terminal
        print("Now getting page %d ..." % i)
        time.sleep(2)
        # make scraper take a longer break to fool their server
        if (i == 9) or (i == 16) or (i == 25):
            time.sleep(10)
            print("Sleeping ...")

# open file for writing
p = open("food_urls.txt", "w")
# run the function that contains other functions
get_all_urls(site, start, end)
# close text file containing all URLs
p.close()
# later - run this using the text file to get each food page
# get_food_details()
