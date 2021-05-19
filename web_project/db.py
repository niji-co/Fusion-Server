import pymongo

from pymongo import MongoClient

def connect_to_mongo(connectionString):
    # Connect to a mongo client using the given connection string
    return MongoClient(connectionString)