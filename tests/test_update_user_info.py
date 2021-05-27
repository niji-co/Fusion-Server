import pymongo

from web_project.db import update_user_info, search_for_user, user

user_details = {
    'course_name': 'GDT',
    'email': 'ryantanzr.work@gmail.com',
    'name': 'Ryan Tan Zheng Rong'
}

def test_update_user_info():
    search_for_user(user_details['course_name'] ,user_details['email']) #init the program
    update_operation = update_user_info('name', user_details['name']) #update username
    #Check for if the operation got acknowledged and if a data entry got modified
    assert update_operation.acknowledged is True
    assert update_operation.modified_count > 0
