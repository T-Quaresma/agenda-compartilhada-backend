from flask_openapi3 import APIBlueprint
from schemas.usuario import User_Creation, User_Search, User_Delete, User_Auth
from services.usuario import credential_check, user_creation, user_search, user_delete
from tags import user_tag
from flask import g
from services.auth import validate_access_token
from utils.auth import require_auth

bp_user = APIBlueprint("user", __name__)

@bp_user.post('/usuario', tags=[user_tag])
def register_user(body: User_Creation):
    try:
        result, status = user_creation(body)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}"), 400
        return {"Message": "Error creating user."}, 400

@bp_user.get('/usuarios', tags=[user_tag])
def search_user(query: User_Search):
    try:
        result, status = user_search(query)
        return result, status 
    except Exception as e: 
        print(f"Error: {str(e)}")
        return {"Message": "Error searching user."}, 500
    
@bp_user.delete('/usuario', tags=[user_tag])
def delete_user(body: User_Delete):
    try:
        result = user_delete(body)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error deleting the user."}, 400

@bp_user.post('/auth/verify', tags=[user_tag])
def verify_user(body:User_Auth):
    try:
        result, status = credential_check(body)
        return result, status   
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error verifying the user."}, 500

