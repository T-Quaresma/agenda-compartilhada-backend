from database import db
from models import Usuario

# Creating User and adding it to the database.
def user_creation(data):
    new_user = Usuario(
        nomeUsu = data.name,
        email = data.email,
        senha = data.senha
    )
    db.session.add(new_user)
    db.session.commit()
    return {"Message": "User created successfully!"}

# Searching for a specific user.

def user_search(data):
    users = db.session.execute(db.select(Usuario).where(Usuario.nomeUsu == data.name)).scalars().all()
    if not users:
        return {"Message": "User not found."}
    user_list = []
    for user in users:
        user_list.append({"nomeUsu": user.nomeUsu, "usuId": user.usuId, "email": user.email})
    return user_list

# User can only delete their own user so it's a direct approach

def user_delete(data):
    user = db.session.execute(db.select(Usuario).where(Usuario.usuId == data.id)).scalars().first()
    if user is None:
        return {"Message": "User not found."}
    else:
        db.session.delete(user)
        db.session.commit()
        return {"Message": "User deleted successfully."}