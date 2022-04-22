from pymongo import MongoClient

class Database:

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client.anime_database

    def insert_anime(self, data):
        self.db.animes.insert_one(data)
    
    def find_query(self, query):
        return self.db.animes.find(query)
    
    def update_anime(self, query, new_value):
        self.db.animes.update_one(query, new_value)
    
    def insert_recents(self, data):
        self.db.recents.insert_one(data)
