from flask_openapi3 import APIBlueprint
from schemas.atividade import Activity_Creation, Activity_Delete, Activity_Search, Activity_Update
from services.atividade import create_activity, search_activity, delete_activity, update_activity
from tags import activity_tag
from flask import g
from utils.auth import require_auth

bp_activity = APIBlueprint('activity', __name__)

@bp_activity.post('/activity', tags=[activity_tag])
@require_auth
def creating_activity(body: Activity_Creation):
    print(f"Dados recebidos: {body}")
    try:
        user_id = g.user["usuId"]
        result, status = create_activity(body, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error creating activity."}, 400
    
@bp_activity.get('/activity', tags=[activity_tag])
@require_auth
def searching_activity(query: Activity_Search):
    try:
        user_id = g.user["usuId"]
        result = search_activity(query, user_id)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error searching activities."}, 400
    
@bp_activity.delete('/activity', tags=[activity_tag])
@require_auth
def deleting_activity(body: Activity_Delete):
    try:
        user_id = g.user["usuId"]
        result, status = delete_activity(body, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Activity could not be deleted."}, 400

@bp_activity.put('/activity', tags=[activity_tag])
@require_auth
def updating_activity(body: Activity_Update):
    try:
        user_id = g.user["usuId"]
        result, status = update_activity(body, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Activity could not be updated."}, 400


    