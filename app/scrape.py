import requests
from bs4 import BeautifulSoup
from environment import URL

response = requests.get(url=URL)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
