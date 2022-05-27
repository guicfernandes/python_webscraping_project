import requests
import pprint
from bs4 import BeautifulSoup
from environment import URL


def get_website_object(url):
    # TODO
    # Request the html of a website
    # Parser it into beautifulsoup4 object

    response = requests.get(url=url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selecting a CSS element (selector)
    # '.score' -> the css class called score
    # '#score_31497765' -> the css id called score_31497765
    # print(soup.find(id='score_31497765'))
    # print(soup.title)
    # print(soup.select('.score'))
    return soup


def get_website_links(soup_object):
    # TODO
    # Grab all the elements with the css class '.titlelink' -> Story Titles
    links = soup_object.select('.titlelink')
    print(f'type of links {type(links)}')
    return links


def get_website_subtext(soup_object):
    # TODO
    # Grab all the elements with the css classe '.score' -> Story scores
    # votes = soup.select('.score')
    subtext = soup_object.select('.subtext')
    print(f'type subtext {type(subtext)}')
    return subtext


def sort_stories_by_votes(list):
    # TODO
    # Sort list of objects ordered by votes in reverse
    return sorted(
        list,
        key=lambda k: k['votes'],
        reverse=True
    )


def create_custom_website(links, subtext):
    # TODO
    # Grab the hyper link of every story with a score greater than 100
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

    return sort_stories_by_votes(website)


if __name__ == '__main__':
    links = []
    subtext = []
    i = 1
    for page in URL:
        print(f'iteracao {i}')
        soup = get_website_object(page)
        links = links + get_website_links(soup)
        print(f'type links for {links}')
        subtext = subtext + get_website_subtext(soup)
        i = i+1
    pprint.pprint(create_custom_website(links, subtext))
