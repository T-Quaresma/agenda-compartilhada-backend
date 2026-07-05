from flask_openapi3 import APIBlueprint
from schemas.agendamento import Schedule_Creation, Schedule_Delete, Schedule_Search, Schedule_Update
from services.agendamento import create_schedule, list_schedules, delete_schedule, delete_all_schedules, update_schedule
from tags import schedule_tag

bp_schedule = APIBlueprint("schedules", __name__)

@bp_schedule.post('/schedule', tags=[schedule_tag])
def creating_schedule(body: Schedule_Creation):
    try:
        result = create_schedule(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return{"Message": "Error creating schedule"}, 400
    
@bp_schedule.get('/schedule', tags=[schedule_tag])
def list_schedule(query: Schedule_Search):
    try:
        result = list_schedules(query)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}')
        return{"Message": "Error seaching schedules."}, 400
    
@bp_schedule.delete('/schedule', tags=[schedule_tag])
def deleting_schedule(body: Schedule_Delete):
    try:
        result = delete_schedule(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}'), 400
        return{"Message": "Error deleting schedule."}, 400
    
@bp_schedule.put('/schedule', tags=[schedule_tag])
def updating_schedule(body: Schedule_Update):
    try: 
        result = update_schedule(body)
        return result, 200
    except Exception as e:
        print(f'Error: {str(e)}'), 400
        return{"Message": "Error updating schedule"}, 400
    
#@bp_schedule.delete('/schedule', tags=[schedule_tag])
#def deleting_schedules(body: Schedule_Delete):
#    try: 
#        result = delete_all_schedules(body)
#        return result, 200
#    except Exception as e:
#        print(f'Error: {str(e)}')
 #       return{"Message": "Error deleting schedules."}, 400
