from flask_openapi3 import APIBlueprint
from schemas.grupo import Group_Creation, Group_Search, Group_Delete, Group_Update
from services.grupo import create_group, search_group, delete_group, update_group
from tags import group_tag

bp_group = APIBlueprint("groups", __name__)

@bp_group.post('/group', tags=[group_tag])
def creating_group(body: Group_Creation):
    try:
        result = create_group(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error creating group."}, 400

@bp_group.get('/group', tags=[group_tag])
def searching_group(query: Group_Search):
    try:
        result = search_group(query)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error searching groups."}, 400

@bp_group.delete('/group', tags=[group_tag])
def deleting_group(body: Group_Delete):
    try:
        result = delete_group(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error deleting group."}, 400
    
@bp_group.put('/group', tags=[group_tag])
def updating_group(body: Group_Update):
    try:
        result = update_group(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error updating group."}, 400