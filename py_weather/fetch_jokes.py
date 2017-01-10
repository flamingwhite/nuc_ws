import requests
import bs4


def top_jokes(n=5):
    url = 'http://www.budejie.com/text/'
    soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
    jokes = [j.text for j in soup.select('.j-r-list-c-desc')][:n]
    return jokes

# top_jokes()
