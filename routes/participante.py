from flask_openapi3 import APIBlueprint
from schemas.participante import Participant_Addition, Participant_Delete, Participant_Search
from services.participante import add_participant, delete_participant, select_participant
from tags import participant_tag
from flask import g
from utils.auth import require_auth

bp_participant = APIBlueprint('participant', __name__)

@bp_participant.post('/participant', tags=[participant_tag])
@require_auth
def register_participant(body: Participant_Addition):
    try:
        user_id = g.user["usuId"]
        result, status = add_participant(body, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error adding participant."}, 400
    
@bp_participant.get('/participant', tags=[participant_tag])
@require_auth
def participant_search(query: Participant_Search):
    try:
        user_id = g.user["usuId"]
        result, status = select_participant(query, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error searching participants."}, 400

@bp_participant.delete('/participant', tags=[participant_tag])
@require_auth
def participant_deletion(body: Participant_Delete):
    try:
        user_id = g.user["usuId"]
        result, status = delete_participant(body, user_id)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error deleting participant."}, 400

