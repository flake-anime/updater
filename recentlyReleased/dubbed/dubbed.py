from cv2 import detail_ImageFeatures
import requests
from bs4 import BeautifulSoup

class DubbedCrawler:
    def __init__(self, pages):
        self.pages = pages

    def getRecent(self):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        animeDetails = []

        for i in range(self.pages):
            response = requests.get(f"https://ww2.gogoanimes.org/ajax/page-recent-release?page={self.pages}&type=2", headers=header).text
            soup = BeautifulSoup(response, "html.parser")

            div = soup.findAll("div", attrs={"class": "img"})
            a = []

            for i in div:
                aTags = i.findAll("a")
                a.append(aTags)

            for i in a:
                i = str(i).replace("[", "").replace("]", "").replace("<a ", "").replace("/>", "").replace(">", "").replace("<img ", "")
                i = i.replace("<div ", "").replace("</div", "").replace("</a", "").replace("\n", "")
                details = i.replace("href=", "").replace("title=", "").replace("alt=", "").replace('loading="lazy"', "").replace("src=", "")[:-19].split(" ")

                #Last 5 characters incase the episode number is in the thousands lol
                episodeBeginning = details[0][-5:]
                episodeNum = ""

                for i in episodeBeginning:
                    if i.isdigit():
                        episodeNum += i

                gogoID = details[0].replace('"', "").replace("episode-", "").replace(f"{episodeNum}", "").split("/")[2][:-1]
                episodeLink = details[0].replace('"', "")
                imgURL = details[-1].replace('"', "")

                details = {
                    "episode": episodeNum,
                    "ID": gogoID,
                    "link": episodeLink,
                    "imgURL": imgURL
                }

                animeDetails.append(details)

        return animeDetails