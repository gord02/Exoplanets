
import requests

import pprint
from bs4 import BeautifulSoup

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia' 
URL = 'http://exoplanet.eu/catalog/all_fields/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='content content_bg')

# job_elems = results.find_all('section', class_='card-content')

# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem)



# names = results.find_all('tr', class_='odd')
# print(names)
# name1 = results.find_all('td', class_='name')
# print(name1)
# name2 = results.find_all('a')
# print(name2)


# results = soup.find(id='astrotools-ui-container')
# # print(results)
# print(type(results))
# narrow= soup.find(id="astrotools-connection-indicator")
# print(narrow)
# print(type(narrow))

div= results.find('div', class_='dataTables_scrollBody')
print(div)
table = results.find('table', class_='catalog dataTable no-footer')
print(table)


# name3 = results.find_all('h1')
# print(name3)


# try:
#     for name in names:
#         title= name.find('td', class_='name')
#         print(title)
# # except:
# except Exception as err:
#     print("nonr found")
#     print(err)

























# # get the site’s HTML code into your Python script so that you can interact with it
# import requests

# import pprint

# from bs4 import BeautifulSoup


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print("===================================")

# list(soup.children)
# [type(item) for item in list(soup.children)]

# listd=list(soup.children)
# # body = list(html.children)
# # print(listd)
# list(body.children)

