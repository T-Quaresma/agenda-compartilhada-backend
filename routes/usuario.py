from flask_openapi3 import APIBlueprint
from schemas.usuario import User_Creation, User_Search, User_Delete
from services.usuario import user_creation, user_search, user_delete
from tags import user_tag

bp_user = APIBlueprint("user", __name__)

@bp_user.post('/usuario', tags=[user_tag])
def register_user(body: User_Creation):
    try:
        result = user_creation(body)
        return result, 200
    except Exception as e:
        return(f"Error: {str(e)}"), 400
       # return {"Message": "Error creating user."}, 400

@bp_user.get('/usuarios', tags=[user_tag])
def search_user(query: User_Search):
    try:
        result = user_search(query)
        return result, 200
    except Exception as e: 
        return(f"Error: {str(e)}"), 400
       # return {"Message": "User not found."}, 400
    
@bp_user.delete('/usuario', tags=[user_tag])
def delete_user(body: User_Delete):
    try:
        result = user_delete(body)
        return result, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error deleting the user."}, 400