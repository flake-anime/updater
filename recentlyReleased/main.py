from subbed.subbed import SubbedCrawler
from dubbed.dubbed import DubbedCrawler

subbedCrawler = DubbedCrawler(5)
dubbedCrawler = DubbedCrawler(5)

subbedAnimeDetails = subbedCrawler.getRecent()
dubbedAnimeDetails = dubbedCrawler.getRecent()

print(subbedAnimeDetails[0])