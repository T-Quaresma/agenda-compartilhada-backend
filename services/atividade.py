from database import db
from models import Atividade, Grupo

def create_activity(data, user_id):
    if data.group_id is not None:
        group = db.session.execute(db.select(Grupo).where(Grupo.grupoId == data.group_id)).scalars().first()
        if group is None:
            return {
                "Message": "Group not found."
            }, 404
        if group.criadorId != user_id:
            return {
            "Message": "You do not have permission to create an activity in this group."  
            }, 403
    new_activity = Atividade(
        nomeAtiv= data.name,
        descAtiv= data.description,
        criadorId= user_id,
        imagem= data.image,
        grupoId= data.group_id
    )
    db.session.add(new_activity)
    db.session.commit()
    return {
        "Message": "Activity created successfully!",
        "ativId": new_activity.ativId
    }, 201

def search_activity(data, user_id):
    query = db.select(Atividade).where(
        Atividade.criadorId == user_id
    )
    if data.name is not None:
        query = query.where(
            Atividade.nomeAtiv == data.name
        )
    if data.activity_id is not None:
        query = query.where(
            Atividade.ativId == data.activity_id
        )
    if data.group_id is not None:
        query = query.where(
            Atividade.grupoId == data.group_id
        )
    activities = db.session.execute(
        query
    ).scalars().all()
    activity_list = []
    for activity in activities:
        activity_list.append({
            "nomeAtiv": activity.nomeAtiv,
            "ativId": activity.ativId,
            "descAtiv": activity.descAtiv,
            "imagem": activity.imagem,
            "grupoId": activity.grupoId
        })
    return activity_list
    
def delete_activity(data, user_id):
    activity = db.session.execute(
        db.select(Atividade).where(
            Atividade.ativId == data.activity_id
        )
    ).scalars().first()
    if activity is None:
        return {
            "Message": "Activity not found."
        }, 404
    if activity.criadorId != user_id:
        return {
            "Message": "You do not have permission to delete this activity."
        }, 403
    db.session.delete(activity)
    db.session.commit()
    return {
        "Message": "Activity deleted successfully."
    }, 200


def update_activity(data, user_id):
    activity = db.session.execute(
        db.select(Atividade).where(
            Atividade.ativId == data.activity_id
        )
    ).scalars().first()
    if activity is None:
        return {
            "Message": "Activity not found."
        }, 404
    if activity.criadorId != user_id:
        return {
            "Message": "You do not have permission to update this activity."
        }, 403
    if data.group_id is not None:
        group = db.session.execute(
            db.select(Grupo).where(
                Grupo.grupoId == data.group_id
            )
        ).scalars().first()
        if group is None:
            return {
                "Message": "Group not found."
            }, 404
        if group.criadorId != user_id:
            return {
                "Message": "You do not have permission to move this activity to this group."
            }, 403
    if data.name is not None:
        activity.nomeAtiv = data.name
    if data.description is not None:
        activity.descAtiv = data.description
    if data.image is not None:
        activity.imagem = data.image
    if data.group_id is not None:
        activity.grupoId = data.group_id
    db.session.commit()
    return {
        "Message": "Activity updated successfully!"
    }, 200