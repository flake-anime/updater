from database import Database
from engine.recent_anime_scrapper import RecentAnimeScrapper
from engine.iterator import get_complete_anime_info, get_all_episode_details
from dotenv import load_dotenv
from pprint import pprint
from flask import Flask
import os
load_dotenv()

mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')

database = Database(connection_string=mongo_connection_string)
crawler = RecentAnimeScrapper(pages=1)

app = Flask(__name__)

@app.route("/update_database")
def update_database():
    recent_subbed = crawler.get_recent_dubbed()
    recent_dubbed = crawler.get_recent_dubbed()

    # Subbed
    for anime in recent_subbed:
        gogo_id = anime['gogo_id']
        episode_link = anime['episode_link']
        episode_number = anime['episode_number']

        # If anime is not in the database, add it, and add it to recents
        result = database.find_query({'gogo_id': gogo_id})
        if not result:
            anime = get_complete_anime_info(episode_link)
            database.insert_anime(anime)
            database.insert_recents({
                'gogo_id': gogo_id,
                'episode_number': episode_number,
            })

        # If episode does not exist in the anime, add it, and add it to recents
        result_episodes = result[0]['episodes']
        is_episode_exists = False
        for episode in result_episodes:
            if episode['episode_number'] == episode_number:
                is_episode_exists = True
                break

        if not is_episode_exists:
            episode = get_all_episode_details(episode_number, episode_link)
            result_episodes[episode_number] = episode
            database.update_anime({'gogo_id': gogo_id}, {'$set': {'episodes': result_episodes}})
            database.insert_recents({
                'gogo_id': gogo_id,
                'episode_number': episode_number,
            })
    
    # Dubbed
    for anime in recent_dubbed:
        gogo_id = anime['gogo_id']
        episode_link = anime['episode_link']
        episode_number = anime['episode_number']

        # If anime is not in the database, add it, and add it to recents
        result = database.find_query({'gogo_id': gogo_id})
        if not result:
            anime = get_complete_anime_info(episode_link)
            database.insert_anime(anime)
            database.insert_recents({
                'gogo_id': gogo_id,
                'episode_number': episode_number,
            })

        # If episode does not exist in the anime, add it, and add it to recents
        result_episodes = result[0]['episodes']
        is_episode_exists = False
        for episode in result_episodes:
            if episode['episode_number'] == episode_number:
                is_episode_exists = True
                break

        if not is_episode_exists:
            episode = get_all_episode_details(episode_number, episode_link)
            result_episodes[episode_number] = episode
            database.update_anime({'gogo_id': gogo_id}, {'$set': {'episodes': result_episodes}})
            database.insert_recents({
                'gogo_id': gogo_id,
                'episode_number': episode_number,
            })
    
    return "Updated database"

if __name__ == "__main__":
    app.run()