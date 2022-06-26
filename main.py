import requests
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

