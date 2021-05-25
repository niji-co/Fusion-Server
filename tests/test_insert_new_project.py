from dns import name
import pymongo

# import your functions/classes here
from web_project.db import insert_new_project, search_for_user
user_details = {
    'course_name': 'GDT',
    'email': 'ryantanzr.work@gmail.com',
    'name': 'Ryan Tan Zheng Rong'    
}

project_details = {
    'name': 'Crusader-1',
    'description': 'kdgerhgwakfnjbhhqwuriqwfk'
}

def test_insert_new_project():
    search_for_user(user_details['course_name'] ,user_details['email'])
    insertion_result = insert_new_project(project_details['name'])
    
    assert insertion_result.acknowledged is True
    assert insertion_result.modified_count == 1, 'Project did not get inserted'