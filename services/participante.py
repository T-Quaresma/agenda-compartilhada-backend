from database import db
from models import ParticipantesAtiv, Usuario


def add_participant(data):
    new_participant = ParticipantesAtiv(
        usuId = data.user_id,
        agenId = data.schedule_id
    )
    db.session.add(new_participant)
    db.session.commit()
    return {"Message": "New participant added."}

def select_participant(data):
    participants = db.session.execute(db.select(ParticipantesAtiv).join(Usuario, ParticipantesAtiv.usuId == Usuario.usuId).where(Usuario.nomeUsu == data.user_name)).scalars().all()
    participant_list = []
    if not participants:
        return {"Message": "User was not found."}
    else:
        for participant in participants:
            participant_list.append({"nomeUsu": participant.usuario.nomeUsu, "usuId": participant.usuario.usuId, "partId": participant.partId})
        return participant_list
    
def delete_participant(data):
    participant = db.session.execute(db.select(ParticipantesAtiv).where(ParticipantesAtiv.partId == data.id)).scalars().first()
    if participant is None:
        return {"Message": "User was not found."}
    else:
        db.session.delete(participant)
        db.session.commit()
        return {"Message": "User removed from the activity."}