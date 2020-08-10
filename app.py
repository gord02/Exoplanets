from flask import Flask
from flask import render_template



# get the site’s HTML code into your Python script so that you can interact with it
import requests

import pprint

from bs4 import BeautifulSoup


app = Flask(__name__)

# This code performs an HTTP request to the given URL. It retrieves the HTML data that the server sends back and stores that data in a Python object.
# URL = 'http://exoplanet.eu/catalog/'
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# this creates a beautfiul soup object
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

results = soup.find(id='ResultsContainer')
names = results.find_all('td')


job_elems = results.find_all('tr', class_='odd')


job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()









# For easier viewing, you can .prettify() any Beautiful Soup object when you print it out
# print(names.prettify())

# for name in names:
#     print(name, end='\n'*2)



# pprint(page)
# print(page.contentpprint())

# pprint.pprint("Hello pretty printer")
# my_printer = pprint.PrettyPrinter()
# my_printer.pprint(page.content)


@app.route("/")
def index():
    # 
    return render_template("index.html")

@app.route("/<exoplanet>")
def show():
    return render_template("show.html")

# # ================================
# # For scrapping
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd

# # To configure webdriver to use Chrome browser, we have to set the path to chromedriver
# # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# driver = webdriver.Chrome('/path/to/chromedriver')

# name=[] #List to store name of the exoplanets
# distance=[] #List to store LIGHT-YEARS from earht of the exoplanets
# mass=[] #List to store mass of the exoplanets
# stelMag=[] #List to store rating of the exoplanets
# dd=[] #List to store discrovery date of the exoplanets


# # Opens URL to website to be scrapped
# driver.get("https://exoplanets.nasa.gov/exoplanet-catalog/")

# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):

# # the attrs or attributes are the classes on the elemnt you are searching for
# # name=a.find('div', attrs={'class':'_3wU53n'})
#     name=a.find('a', attrs={})
#     # price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#     # rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#     name.append(name.text)
# # prices.append(price.text)
# # ratings.append(rating.text) 

# for a in name:
#     print(a)
