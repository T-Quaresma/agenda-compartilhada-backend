from flask_openapi3 import APIBlueprint
from schemas.agendamento import Schedule_Creation, Schedule_Delete, Schedule_Search, Schedule_Update
from services.agendamento import create_schedule, list_schedules, delete_schedule, delete_all_schedules, update_schedule
from tags import schedule_tag
from flask import g
from utils.auth import require_auth

bp_schedule = APIBlueprint("schedules", __name__)

@bp_schedule.post('/schedule', tags=[schedule_tag])
@require_auth
def creating_schedule(body: Schedule_Creation):
    try:
        user_id = g.user["usuId"]
        result, status = create_schedule(body, user_id)
        return result, status
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error creating schedule."}, 400
    
@bp_schedule.get('/schedule', tags=[schedule_tag])
@require_auth
def list_schedule(query: Schedule_Search):
    try:
        user_id = g.user["usuId"]
        result = list_schedules(query, user_id)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error searching schedules."}, 400
    
@bp_schedule.delete('/schedule', tags=[schedule_tag])
@require_auth
def deleting_schedule(body: Schedule_Delete):
    try:
        user_id = g.user["usuId"]
        result, status = delete_schedule(body, user_id)
        return result, status
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error deleting schedule."}, 400
    
@bp_schedule.put('/schedule', tags=[schedule_tag])
@require_auth
def updating_schedule(body: Schedule_Update):
    try:
        user_id = g.user["usuId"]
        result, status = update_schedule(body, user_id)
        return result, status
    except Exception as e:
        print(f'Error: {str(e)}')
        return {"Message": "Error updating schedule."}, 400
    

