from data_crawling import parser, crawling
from summarizes import summarizes
import pandas as pd
from datetime import date


url = 'https://search.hani.co.kr/Search?command=query&keyword=%ED%95%B4%EC%96%91%EC%98%A4%EC%97%BC&sort=d&period=all&datefrom=1988.01.01&dateto=' + '.'.join(str(date.today()).split('-')) + '&media=news'


def main(url):
    titles, urls = parser(url)
    contents = []
    summary = []

    for i in urls:
        contents.append(crawling(i))

    for content in contents:
        summary.append(summarizes(content))

    # lists to dataframe & to json
    df = pd.DataFrame({'title': titles, 'link': urls, 'content': contents, 'summary': summary})
    js = df['summary'].to_json(force_ascii = False, indent = 4)
    
    return js
