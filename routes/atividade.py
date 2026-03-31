from flask_openapi3 import APIBlueprint
from schemas.atividade import Activity_Creation, Activity_Delete, Activity_Search
from services.atividade import create_activity, search_activity, delete_activity
from tags import activity_tag

bp_activity = APIBlueprint('activity', __name__)

@bp_activity.post('/activity', tags=[activity_tag])
def creating_activity(body: Activity_Creation):
    print(f"Dados recebidos: {body}")
    try:
        result = create_activity(body)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return{"Message:" "Error creating user."}, 400
    
@bp_activity.get('/activity', tags=[activity_tag])
def searching_activity(query: Activity_Search):
    try:
        result = search_activity(query)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return{"Message:" "Activity not found."}, 400
    
@bp_activity.delete('/activity', tags=[activity_tag])
def deleting_activity(body: Activity_Delete):
    try:
        result = delete_activity(body)
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        return{"Message:" "Activity could not be deleted."}, 400


    