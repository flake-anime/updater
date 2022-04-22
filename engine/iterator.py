from engine.scrappers.gogoanime_scrapper import GogoAnimeScrapper

scrapper = GogoAnimeScrapper()

def get_all_episode_details(episode_number, episode_link, proxies = None):
    player_link = scrapper.get_player_link(episode_link, proxies)

    download_link = None
    if player_link is not None:
        download_link = scrapper.get_download_link(player_link)

    episode = {
        "episode_number": episode_number,
        "episode_link": episode_link,
        "player_link": player_link,
        "download_link": download_link,
    }

    return episode

def get_complete_anime_info(anime_link, proxies = None):
    anime_info = scrapper.get_anime_info(anime_link, proxies)
    episode_links = scrapper.get_episodes(anime_link, proxies)
    
    episodes = []

    for episode_link in episode_links:
        episode_number = episode_link['episode_number']
        episode_link = episode_link['episode_link']
        episode = get_all_episode_details(episode_number, episode_link, proxies)
        episodes.append(episode)

    anime_info['episodes'] = episodes

    return anime_info