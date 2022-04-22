from pymongo import MongoClient

class Database:

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client.anime_database

    def insert_anime(self, data):
        self.db.anime_collection.insert_one(data)
    
    def find_query(self, query):
        return self.db.anime_collection.find(query)
    
    def update_anime(self, query, new_value):
        self.db.anime_collection.update_one(query, new_value)
