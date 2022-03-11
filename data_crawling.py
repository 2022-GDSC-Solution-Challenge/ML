from bs4 import BeautifulSoup
import requests


def parser(url):
    response = requests.get(url)
    title = []
    url = []
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pa = soup.find_all('dt')
    for t in pa:
        if len(t) <= 0:  # Case with no text during parsing
            continue
        else:
            title.append(t.get_text().strip())
            url.append(t.find('a')['href'])

    return title, url


def crawling(url):
    contents = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select('#a-left-scroll-in > div.article-text > div > div.text')
    contents.append(content[0].get_text())

    return contents