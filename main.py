from engine.recent_anime_scrapper import RecentAnimeScrapper
from pprint import pprint

crawler = RecentAnimeScrapper(pages=1)

recent_subbed = crawler.get_recent_dubbed()
recent_dubbed = crawler.get_recent_dubbed()

pprint(recent_subbed)
pprint(recent_dubbed)