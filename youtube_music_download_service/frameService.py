import re

from bs4 import BeautifulSoup
import requests

url = 'http://weibo.com/2239529624/En0IU3nLQ?filter=hot&root_comment_id=0&type=comment'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}

with requests.Session() as session:
    session.headers = headers

    response = session.get(url)

    soup = BeautifulSoup(response.content)

    # follow the iframe url
    response = session.get('http:' + soup.iframe['src'], headers={'Referer': url})
    soup = BeautifulSoup(response.content)

    # extract the video URL from the script tag
    print(re.search(r'"url":"(.*?)"', soup.script.text).group(1))