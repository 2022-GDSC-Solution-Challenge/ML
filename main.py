from data_crawling import crawling
from summarizes import summarizes


def main(url):
    contents = []
    summary = []
    contents.append(crawling(url))

    for content in contents:
        summary.append(summarizes(content))

    return ''.join(summary[0])
