from database import db
from models import Atividade

def create_activity(data):
    new_activity = Atividade(
        nomeAtiv = data.name,
        descAtiv = data.description,
        criadorId = data.user_id
    )
    db.session.add(new_activity)
    db.session.commit()
    return {"Message": "Activity created successfully!"}

def search_activity(data):
    activities = db.session.execute(db.select(Atividade).where(Atividade.nomeAtiv == data.name)).scalars().all()
    activity_list = []
    if not activities:
        return {"Message": "Activity not found."}
    else:
        for activity in activities:
            activity_list.append({"nomeAtiv": activity.nomeAtiv, "ativId": activity.ativId})
        return activity_list
    
def delete_activity(data):
    activity = db.session.execute(db.select(Atividade).where(Atividade.ativId == data.activity_id)).scalars().first()
    if activity is None:
        return {"Message": "Activity not found."}
    else:
        db.session.delete(activity)
        db.session.commit()
        return {"Message": "Activity deleted successfully."}