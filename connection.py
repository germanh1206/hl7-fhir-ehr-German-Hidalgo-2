from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://gahalvarado641:German1206@informationpatient.v31lg.mongodb.net/?retryWrites=true&w=majority&appName=InformationPatient"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
