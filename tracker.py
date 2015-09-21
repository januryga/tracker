#Tracker

import requests
from cssselect import HTMLTranslator
from lxml import html
from sys import exit


def get_news_items(url, css_selector):
# Returns array of news item Elements with given css_selector from given url.
    page = requests.get(url)
    tree = html.fromstring(page.text)

    expression = HTMLTranslator().css_to_xpath(css_selector)
    extract = [e.text_content() for e in tree.xpath(expression)]
    return extract

news = get_news_items('http://chelmiec.pl/aktualnosci.html', 'div.news')
printable_news = [item.encode('ascii', 'ignore') for item in news]
print(printable_news)
