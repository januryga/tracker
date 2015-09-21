#Tracker

import requests
from cssselect import HTMLTranslator
from lxml import html
from sys import exit

page = requests.get('http://www.example.com')
tree = html.fromstring(page.text)

def get_content_of(css_selector):
# Returns text contents of html elements specified with a css selector
    expression = HTMLTranslator().css_to_xpath(css_selector)
    extract = [e.text_content() for e in tree.xpath(expression)]
    return extract

title = get_content_of('div > h1')
print(title)
