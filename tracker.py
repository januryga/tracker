#Tracker

import requests
from cssselect import HTMLTranslator
from lxml import html
from sys import exit

gminy = {
    'chelmiec': {
        'url': 'http://chelmiec.pl/aktualnosci.html',
        'news_item_path': 'div.news',
        'title_path': 'div.newstyt',
    }
}

def xpath(css_selector):
#Convert CSS selector to XPath
    path = HTMLTranslator().css_to_xpath(css_selector)
    return path

def get_news_items(url, css_selector):
# Returns array of news item Elements with given css_selector from given url.
    page = requests.get(url)
    tree = html.fromstring(page.text)
    expression = xpath(css_selector)

    extracted_news_items = tree.xpath(expression)
    return extracted_news_items

def get_title(news_item, css_selector):
    css_path = xpath(css_selector)
    match = news_item.xpath(css_path)
    title = match[0].text_content() #xpath returns an array, hence [0]
    return title

def strip(string):
    return string.encode('ascii', 'ignore')

news = get_news_items('http://chelmiec.pl/aktualnosci.html', 'div.news')
titles = [get_title(item, 'div.newstyt') for item in news]
clean_titles = [strip(title) for title in titles]
print(clean_titles)
