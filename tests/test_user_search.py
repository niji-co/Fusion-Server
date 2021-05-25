import pymongo

# import your functions/classes here
from web_project.db import search_for_user

user_details = {
    'course_name': 'GDT',
    'email': 'ryantanzr.work@gmail.com'    
}

def test_user_search():
    user = search_for_user(user_details['course_name'] ,user_details['email'])
    print(user)
    assert user['email'] == user_details['email'], 'User not found, did you check the database?'
