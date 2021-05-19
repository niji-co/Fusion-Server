import pymongo

from pymongo import MongoClient

#tested
def connect_to_mongo(connection_string):
    # Connect to a mongo client using the given connection string
    return MongoClient(connection_string)

#tested
def search_for_user(course_name, email):
    query_result = client["SDM"][course_name].aggregate([{'$match': { 'email': email } } ]) #returns a cursor

    assert query_result is not None #throw an exception if the query fails

    #assigning global variables
    global collection 
    collection = client["SDM"][course_name]

    global user
    user = query_result.next() #returns the document selected by the cursor
    return user

#tested
def update_user_info(field_to_change, new_info):
    update_result = collection.update_one(
        {'email' : user['email'] },
        {"$set" : {field_to_change : new_info } }
        , False)
    return update_result

def update_project_info(field_to_change, new_info):
    project_subfield_to_change = 'projects' + '.$.' + field_to_change #test this
      
    update_result = collection.update_one(
        {'$match': {'email' : user['email'], } },
        {'$set' : { project_subfield_to_change : new_info }}
        )
    return update_result

def insert_new_project(project_name):
    
    insert_result = collection.update_one([
        {'$match': {'email' : user['email'] } },
        {'$push': { 'projects' : { 'name': project_name } } }
        ])
    return insert_result

def delete_project(project_name):
    deletion_result = collection.update_one([
            {'$match': {'email' : user['email'] } },
            {'$pull': { 'projects' : { 'name': project_name } } }
            ])
    return deletion_result

client = connect_to_mongo("mongodb+srv://MongoBongo:BongoBongo@djongoconnectiontest.nlqyc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
collection = None
user = None