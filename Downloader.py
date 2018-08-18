from urllib.request import *
import urllib
import json
from bs4 import BeautifulSoup
import time


def download_html_page_soup(url: str):
    soup = BeautifulSoup(download_html_page(url), 'html5lib')
    return soup


def download_html_page(url: str):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
    res = urlopen(req)
    return res.read()#.decode(errors='replace')
