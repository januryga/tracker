# Tracker by Jan Uryga

import requests
from cssselect import HTMLTranslator
from lxml import html
from sys import exit

# County database
gminy = {
    'chelmiec': {
        'url': 'http://chelmiec.pl/aktualnosci.html',
        'news_path': 'div.news',
        'title_path': 'div.newstyt',
        'link_path': 'a'
    },

    'grodek': {
        'url': 'http://gminagrodek.pl',
        'news_path': 'ul.news_list_mm > li',
        'title_path': 'div.news_list_right > h3 > a',
        'link_path': 'div.news_list_right > a'
    },

    'grybow': {
        'url': 'http://grybow.pl',
        'news_path': 'li > div.RightNewsTitle',
        'title_path': 'a',
        'link_path': 'a'
    }

}

# Helper functions
def xpath(css_selector):
#Convert CSS selector to XPath
    path = HTMLTranslator().css_to_xpath(css_selector)
    return path

def strip(string):
    return string.encode('ascii', 'ignore').decode('ascii')




# Secondary content functions
def load_news_items(url, css_selector):
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

def get_link(news_item, css_selector):
    css_path = xpath(css_selector)
    match = news_item.xpath(css_path)
    link = match[0].attrib['href']  #xpath returns an array, hence [0]
    return link





# Main content function
def news_items(gmina_name):
# Returns list of news items: dicts containing title and url
    gmina = gminy[gmina_name]
    raw_news = load_news_items(gmina['url'], gmina['news_path'])

    news = []
    for item in raw_news:
        raw_title = get_title(item, gmina['title_path'])
        the_title = strip(raw_title)
        raw_link = get_link(item, gmina['link_path'])
        the_link = strip(raw_link)

        post = { 'title': the_title, 'link': the_link }
        news.append(post)

    return news



print(news_items('grybow'))




