#Tracker

import requests
from cssselect import HTMLTranslator
from lxml import html
from sys import exit

page = requests.get('http://www.example.com')
tree = html.fromstring(page.text)
expression = HTMLTranslator().css_to_xpath('div')

#title = tree.xpath(expression + '/text()')
title = [e.text_content() for e in tree.xpath(expression)]
print(title)
