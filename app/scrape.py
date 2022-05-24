import requests
from bs4 import BeautifulSoup
from environment import URL

response = requests.get(url=URL)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

# Selecting a CSS element (selector)
# '.score' -> the css class called score
# '#score_31497765' -> the css id called score_31497765
# print(soup.find(id='score_31497765'))
# print(soup.title)
# print(soup.select('.score'))

# TODO
# Grab the hyper link of every story with a score greater than 100
# Grab all the elements with the css class '.storylink' -> Story Titles
# Grab all the elements with the css classe '.score' -> Story scores
links = soup.select('.storylink')
votes = soup.select('.score')
