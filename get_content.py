from fake_useragent import UserAgent
import requests
from lxml import etree


def get_content(url):
    ua = {'UserAgent': UserAgent().random}
    content = requests.get(url, ua).text
    dom = etree.HTML(content)

    return content, dom
