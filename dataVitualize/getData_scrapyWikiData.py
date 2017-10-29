from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://en.wikipedia.org'
HEADERS = {'User-Agent':'Mozilla/5.0'}

def get_Nobel_soup():
    """Return a parsed tag tree of our Nobel prize page"""
    # Make a request to the Nobel page, setting valid headers
    response = requests.get(
         BASE_URL + '/wiki/List_of_Nobel_laureates',
         headers=HEADERS)
    # Return the content of the response parsed by BeautifulSoup
    return BeautifulSoup(response.content, "lxml")

soup = get_Nobel_soup()
soup.find('table', {'class':'wikitable sortable'})
soup.find('table': {'class':'sortable wikitable'})
soup.select('table.sortable.wikitable')

table = soup.select_one('table.sortable.wikitable')
table.select('th')
table('th')
