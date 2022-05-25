from os import link
import requests
import pprint
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
links = soup.select('.titlelink')
# votes = soup.select('.score')
subtext = soup.select('.subtext')


def create_custom_website(links, subtext):
    website = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                website.append(
                    {
                        'title': title,
                        'link': href,
                        'votes': points
                    }
                )

    return website


pprint.pprint(create_custom_website(links, subtext))
