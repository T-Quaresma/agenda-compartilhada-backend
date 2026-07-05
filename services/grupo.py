from database import db
from models import Grupo

def create_group(data):
    new_group = Grupo(
        nomeGrupo = data.name,
        criadorId = data.user_id,
        imagem = data.image
    )
    db.session.add(new_group)
    db.session.commit()
    return {"Message": "Group created successfully!", "grupoId": new_group.grupoId}

def search_group(data):
    query = db.select(Grupo)
    if data.user_id:
        query = query.where(Grupo.criadorId == data.user_id)
    if data.group_id:
        query = query.where(Grupo.grupoId == data.group_id)
    groups = db.session.execute(query).scalars().all()
    group_list = []
    if not groups:
        return []
    else: 
        for group in groups:
            group_list.append({"grupoId": group.grupoId, "nomeGrupo": group.nomeGrupo, "imagem": group.imagem})
        return group_list

def delete_group(data):
    group = db.session.execute(db.select(Grupo).where(Grupo.grupoId == data.group_id)).scalars().first()
    if group is None:
        return {"Message": "Group not found."}
    else:
        db.session.delete(group)
        db.session.commit()
        return {"Message": "Group deleted successfully."}
    
def update_group(data):
    group = db.session.execute(db.select(Grupo).where(Grupo.grupoId == data.group_id)).scalars().first()
    if group is None:
        return {"Message": "Group not found."}
    if data.name: 
        group.nomeGrupo = data.name
    if data.image:
        group.imagem = data.image
    db.session.commit()
    return {"Message": "Group updated successfully."}