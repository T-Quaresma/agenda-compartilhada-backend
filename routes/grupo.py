from flask_openapi3 import APIBlueprint
from schemas.grupo import Group_Creation, Group_Search, Group_Delete, Group_Update
from services.grupo import create_group, search_group, delete_group, update_group
from tags import group_tag
from flask import g
from utils.auth import require_auth


bp_group = APIBlueprint("groups", __name__)

@bp_group.post('/group', tags=[group_tag])
@require_auth
def creating_group(body: Group_Creation):
    try:
        user_id = g.user["usuId"]
        result = create_group(body, user_id)
        return result, 201
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error creating group."}, 400

@bp_group.get('/group', tags=[group_tag])
@require_auth
def searching_group(query: Group_Search):
    try:
        user_id = g.user["usuId"]
        result = search_group(query, user_id)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error searching groups."}, 400

@bp_group.delete('/group', tags=[group_tag])
@require_auth
def deleting_group(body: Group_Delete):
    try:
        user_id = g.user["usuId"]
        result, status = delete_group(body, user_id)
        return result, status
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error deleting group."}, 400
    
@bp_group.put('/group', tags=[group_tag])
@require_auth
def updating_group(body: Group_Update):
    try:
        user_id = g.user["usuId"]
        result, status = update_group(body, user_id)
        return result, status
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error updating group."}, 400