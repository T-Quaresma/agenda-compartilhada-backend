from flask_openapi3 import APIBlueprint
from schemas.participante import Participant_Addition, Participant_Delete, Participant_Search
from services.participante import add_participant, delete_participant, select_participant
from tags import participant_tag

bp_participant = APIBlueprint('participant', __name__)

@bp_participant.post('/participant', tags=[participant_tag])
def register_participant(body: Participant_Addition):
    try:
        result = add_participant(body)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error creating user."}, 400
    
@bp_participant.get('/participant', tags=[participant_tag])
def participant_search(query: Participant_Search):
    try:
        result = select_participant(query)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Participant not found."}, 400

@bp_participant.delete('/participant', tags=[participant_tag])
def participant_deletion(body: Participant_Delete):
    try: 
        result = delete_participant(body)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return{"Message": "Error deleting the user"}, 400


