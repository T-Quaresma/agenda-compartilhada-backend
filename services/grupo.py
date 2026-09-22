from database import db
from models import Grupo

def create_group(data, user_id):
    new_group = Grupo(
        nomeGrupo = data.name,
        criadorId = user_id,
        imagem = data.image
    )
    db.session.add(new_group)
    db.session.commit()
    return {"Message": "Group created successfully!", "grupoId": new_group.grupoId}

def search_group(data, user_id):
    query = db.select(Grupo).where(Grupo.criadorId == user_id)
    if data.group_id is not None:
        query = query.where(Grupo.grupoId == data.group_id)
    groups = db.session.execute(query).scalars().all()
    group_list = []
    for group in groups:
        group_list.append({
            "grupoId": group.grupoId,
            "nomeGrupo": group.nomeGrupo,
            "imagem": group.imagem
        })
    return group_list

def delete_group(data, user_id):
    group = db.session.execute(db.select(Grupo).where(Grupo.grupoId == data.group_id)).scalars().first()
    if group is None:
        return {"Message": "Group not found."}, 404
    if group.criadorId != user_id:
        return {
            "Message": "You do not have permission to delete this group"
        }, 403
    db.session.delete(group)
    db.session.commit()
    return {"Message": "Group deleted successfully."}, 200
    
def update_group(data, user_id):
    group = db.session.execute(db.select(Grupo).where(Grupo.grupoId == data.group_id)).scalars().first()
    if group is None:
        return {"Message": "Group not found."}, 404
    if group.criadorId != user_id:
        return {
           "Message": "You do not have permission to update this group." 
        }, 403
    if data.name is not None: 
        group.nomeGrupo = data.name
    if data.image is not None:
        group.imagem = data.image
    db.session.commit()
    return {"Message": "Group updated successfully."}, 200