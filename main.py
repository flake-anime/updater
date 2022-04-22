from engine.recent_anime_scrapper import RecentAnimeScrapper

crawler = RecentAnimeScrapper(pages=1)

recent_subbed = crawler.get_recent_dubbed()
recent_dubbed = crawler.get_recent_dubbed()

print(recent_subbed)
print(recent_dubbed)