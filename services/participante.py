from database import db
from models import ParticipantesAtiv, Usuario, Agendamento


def add_participant(data, user_id):
    schedule = db.session.execute(
        db.select(Agendamento).where(
            Agendamento.agenId == data.schedule_id
        )
    ).scalars().first()
    if schedule is None:
        return {
            "Message": "Schedule not found."
        }, 404
    if schedule.atividade.criadorId != user_id:
        return {
            "Message": "You do not have permission to add participants to this schedule."
        }, 403
    participant_user = db.session.execute(
        db.select(Usuario).where(
            Usuario.usuId == data.user_id
        )
    ).scalars().first()
    if participant_user is None:
        return {
            "Message": "User not found."
        }, 404
    existing_participant = db.session.execute(
        db.select(ParticipantesAtiv).where(
            ParticipantesAtiv.usuId == data.user_id,
            ParticipantesAtiv.agenId == data.schedule_id
        )
    ).scalars().first()
    if existing_participant is not None:
        return {
            "Message": "User is already a participant."
        }, 409
    new_participant = ParticipantesAtiv(
        usuId=data.user_id,
        agenId=data.schedule_id
    )
    db.session.add(new_participant)
    db.session.commit()
    return {
        "Message": "New participant added."
    }, 201

def select_participant(data, user_id):
    schedule = db.session.execute(
        db.select(Agendamento).where(
            Agendamento.agenId == data.schedule_id
        )
    ).scalars().first()
    if schedule is None:
        return {
            "Message": "Schedule not found."
        }, 404
    if schedule.atividade.criadorId != user_id:
        return {
            "Message": "You do not have permission to view participants from this schedule."
        }, 403
    participants = db.session.execute(
        db.select(ParticipantesAtiv)
        .where(
            ParticipantesAtiv.agenId == data.schedule_id
        )
    ).scalars().all()
    participant_list = []
    for participant in participants:
        participant_list.append({
            "nomeUsu": participant.usuario.nomeUsu,
            "usuId": participant.usuario.usuId,
            "partId": participant.partId
        })
    return participant_list, 200
    
def delete_participant(data, user_id):
    participant = db.session.execute(
        db.select(ParticipantesAtiv).where(
            ParticipantesAtiv.partId == data.id
        )
    ).scalars().first()
    if participant is None:
        return {
            "Message": "Participant not found."
        }, 404
    schedule = db.session.execute(
        db.select(Agendamento).where(
            Agendamento.agenId == participant.agenId
        )
    ).scalars().first()
    if schedule is None:
        return {
            "Message": "Schedule not found."
        }, 404
    if schedule.atividade.criadorId != user_id:
        return {
            "Message": "You do not have permission to remove this participant."
        }, 403
    db.session.delete(participant)
    db.session.commit()
    return {
        "Message": "Participant removed successfully."
    }, 200