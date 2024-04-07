from typing import List, Optional
import pymongo
from pymongo import IndexModel

def get_client(host="localhost", port =27017):
    client = pymongo.MongoClient(host, port)
    return client

def get_database(client, database_name="books_database"):
    db = client[database_name]
    return db

def get_collection(db, collection_name, index_models: Optional[List[IndexModel]]=None):
    collection = db[collection_name].create_indexes(
        index_models
    )
    return collection