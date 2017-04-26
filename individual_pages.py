from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import csv

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8,it;q=0.6',
       'Connection': 'keep-alive'}

site = "http://slimdoggy.com/dogfood/dry/acana-adult-large-breed/"

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

# WRITE CODE IN THIS FUNCTION
# get data from each detail page and write it to a csv file
def get_food_details():
    # start a loop to read your urls, trying to put URLs in dict called food_list
    #for url in url_list:
        # open a url from a line in the file
        html = urlopen(site)
        # run the function open_page(site) on that to get bsObj
        open_page(site)
        # use bsbj to extract the individual data items abut this one dog food
        # get name
        name = bsObj.find("h1")[1]
        # get category
        table_1 = bsObj.find("table")
        cat = table_1.find("td")[2]
        # get brand
        brand = table_1.find("td")[4]
        # get protein
        table_2 = bsObj.find("table")[1]
        protein = table_2.find("td")[2]
        # get ingredients
        table_4 = bsObj.find("table")[3]
        ingredients = table_4.find("td")[1]

        # append the items to a python list to create one row for one dog food
        food_details = [name, cat, brand, protein, ingredients]
        row = []
        for detail in food_details:
            try:
                row.append(detail.get_text())
            except:
                row.append("N/A")
        # write the row to the CSV file - c.writerow( row )
        c.writerow(row)
        # repeat


# open a file for writing
csvfile = open("dogfood.csv", 'w')
c = csv.writer(csvfile)
# write the header row for CSV file
c.writerow( ['name', 'cat', 'brand', 'protein', 'ingredients'] )
# run your function
get_food_details()
# close the CSV file and save it
csvfile.close()
