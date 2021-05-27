import pymongo

from pymongo import MongoClient
from web_project.db import connect_to_mongo

# connection test via document find of a sample database/collection
def test_connection():
    client = connect_to_mongo("mongodb+srv://MongoBongo:BongoBongo@djongoconnectiontest.nlqyc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    assert client['sample_airbnb']['listingsAndReviews'].find_one() is not None, \
           "Document not found"
