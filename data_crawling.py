from bs4 import BeautifulSoup
import requests


def crawling(url):
    contents = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select('#a-left-scroll-in > div.article-text > div > div.text')
    contents.append(content[0].get_text())

    return contents