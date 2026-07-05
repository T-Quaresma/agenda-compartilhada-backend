from database import db
from models import Atividade

def create_activity(data):
    new_activity = Atividade(
        nomeAtiv = data.name,
        descAtiv = data.description,
        criadorId = data.user_id,
        imagem = data.image,
        grupoId = data.group_id
    )
    db.session.add(new_activity)
    db.session.commit()
    return {"Message": "Activity created successfully!"}

def search_activity(data):
    query = db.select(Atividade)
    if data.name:
        query = query.where(Atividade.nomeAtiv == data.name)
    if data.user_id:
        query = query.where(Atividade.criadorId == data.user_id)
    if data.activity_id:
        query = query.where(Atividade.ativId == data.activity_id)
    activities = db.session.execute(query).scalars().all()
    activity_list = []
    if not activities:
        return []
    else:
        for activity in activities:
            activity_list.append({"nomeAtiv": activity.nomeAtiv, "ativId": activity.ativId, "descAtiv": activity.descAtiv, "imagem": activity.imagem, "grupoId": activity.grupoId})
        return activity_list
    
def delete_activity(data):
    activity = db.session.execute(db.select(Atividade).where(Atividade.ativId == data.activity_id)).scalars().first()
    if activity is None:
        return {"Message": "Activity not found."}
    else:
        db.session.delete(activity)
        db.session.commit()
        return {"Message": "Activity deleted successfully."}


def update_activity(data):
    activity = db.session.execute(db.select(Atividade).where(Atividade.ativId == data.activity_id)).scalars().first()
    if activity is None:
        return {"Message": "Activity not Found."}
    else:
        if data.name:
            activity.nomeAtiv = data.name
        if data.description:
            activity.descAtiv = data.description
        if data.image:
            activity.imagem = data.image
        if data.group_id:
            activity.groupId = data.group_id
        db.session.commit()
        return {"Message": "Activity updated sucessfully!"}