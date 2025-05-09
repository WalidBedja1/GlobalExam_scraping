# Interface avec MongoDB

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

class MongoRepo:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.collection = self.client[DB_NAME][COLLECTION_NAME]

    def find_answer(self, question):
        # Cherche si une question est déjà en base
        result = self.collection.find_one({"question": question})
        return result["answer"] if result else None

    def save_answer(self, question, answer):
        # Sauvegarde une nouvelle question/réponse
        self.collection.insert_one({
            "question": question,
            "answer": answer
        })
