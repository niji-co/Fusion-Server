import pymongo

# import your functions/classes here
from web_project.db import update_user_info, search_for_user, user

user_details = {
    "course_name": "GDT",
    "email": "ryantanzr.work@gmail.com",
    "name": "Ryan Tan Zheng Rong"    
}

def test_update_user_info():
    search_for_user(user_details["course_name"] ,user_details["email"])
    update_operation = update_user_info("name", user_details["name"])
    
    assert update_operation.acknowledged is True
    assert update_operation.modified_count > 0