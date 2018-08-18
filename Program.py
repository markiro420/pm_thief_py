from Downloader import *
from Parser import *

soup = download_html_page_soup("https://www.parimatch.com/")
hieararchy = get_sport_hierarchy(soup)