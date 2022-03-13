from data_crawling import crawling
from summarizes import summarizes
import pandas as pd


def main(url):
    contents = []
    summary = []
    contents.append(crawling(url))

    for content in contents:
        summary.append(summarizes(content))

    # lists to dataframe & to json
    df = pd.DataFrame({'content': contents, 'summary': summary})
    js = df['summary'].to_json(force_ascii = False, indent = 4)
    
    return js
