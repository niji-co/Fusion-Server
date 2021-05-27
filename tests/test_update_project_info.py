import pymongo

from web_project.db import update_project_info, search_for_user

user_details = {
    "course_name": "GDT",
    "email": "ryantanzr.work@gmail.com",
    "name": "Ryan Tan Zheng Rong"
}

project_details = {
    "old_name": "J",
    "new_name": "Jotunn",
    "description": "jhgbsuncanjhvscmaxjkhcfngumxhxsefscnxmfh"
}

def test_update_project_info():
    search_for_user(user_details["course_name"] ,user_details["email"])
    update_operation = update_project_info(project_details["old_name"], "name", project_details["new_name"])
    #Check for if the operation got acknowledged and if a data entry got modified
    assert update_operation.acknowledged is True
    assert update_operation.modified_count > 0, "Data did not get updated"

    update_operation = update_project_info(project_details["new_name"], "description", project_details["description"])
    #Check for if the operation got acknowledged and if a data entry got upserted
    assert update_operation.acknowledged is True
    assert update_operation.modified_count > 0, "Data did not get upserted"
