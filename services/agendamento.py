from database import db
from models import Agendamento, Atividade

# creation of a schedule

def create_schedule(data, user_id):
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
            "Message": "You do not have permission to create a schedule for this activity."
        }, 403
    new_schedule = Agendamento(
        nomeAgen=data.name,
        descAgen=data.description,
        ativId=data.activity_id,
        local=data.local,
        data_inicio=data.starting_date,
        data_fim=data.ending_date,
        hora_inicio=data.starting_time,
        hora_fim=data.ending_time,
        frequencia=data.frequency
    )
    db.session.add(new_schedule)
    db.session.commit()
    return {
        "Message": "Schedule created successfully!",
        "agenId": new_schedule.agenId
    }, 201

# searching for a existent schedule from a specific / will return a list of schedules linked to the specific activity

def list_schedules(data, user_id):
    query = (
        db.select(Agendamento)
        .join(
            Atividade,
            Agendamento.ativId == Atividade.ativId
        )
        .where(
            Atividade.criadorId == user_id
        )
    )
    if data.activity_id is not None:
        query = query.where(
            Agendamento.ativId == data.activity_id
        )
    if data.agenId is not None:
        query = query.where(
            Agendamento.agenId == data.agenId
        )
    query = query.order_by(
        Agendamento.data_inicio,
        Agendamento.hora_inicio
    )
    schedules = db.session.execute(
        query
    ).scalars().all()
    schedules_list = []
    for schedule in schedules:
        schedules_list.append({
            "nomeAtiv": schedule.atividade.nomeAtiv,
            "ativId": schedule.ativId,
            "nomeAgen": schedule.nomeAgen,
            "data_inicio": schedule.data_inicio,
            "hora_inicio": str(schedule.hora_inicio) if schedule.hora_inicio else None,
            "data_fim": schedule.data_fim,
            "hora_fim": str(schedule.hora_fim) if schedule.hora_fim else None,
            "frequencia": schedule.frequencia,
            "local": schedule.local,
            "descAgen": schedule.descAgen,
            "agenId": schedule.agenId
        })
    return schedules_list
        
    
# Deleting an existing schedule
    
def delete_schedule(data, user_id):
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
            "Message": "You do not have permission to delete this schedule."
        }, 403
    db.session.delete(schedule)
    db.session.commit()
    return {
        "Message": "Schedule deleted successfully."
    }, 200
    
# Deleting all schedules from a specific activity
    
def delete_all_schedules(data):
    schedules = db.session.execute(
        db.select(Agendamento).where(
            Agendamento.ativId == data.activity_id
        )
    ).scalars().all()
    if not schedules:
        return {
            "Message": "This activity has no schedules at this time."
        }
    for schedule in schedules:
        db.session.delete(schedule)
    db.session.commit()
    return {
        "Message": "All schedules deleted successfully."
    }
    
def update_schedule(data, user_id):
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
            "Message": "You do not have permission to update this schedule."
        }, 403
    if data.name is not None:
        schedule.nomeAgen = data.name
    if data.description is not None:
        schedule.descAgen = data.description
    if data.local is not None:
        schedule.local = data.local
    if data.starting_date is not None:
        schedule.data_inicio = data.starting_date
    if data.ending_date is not None:
        schedule.data_fim = data.ending_date
    if data.starting_time is not None:
        schedule.hora_inicio = data.starting_time
    if data.ending_time is not None:
        schedule.hora_fim = data.ending_time
    if data.frequency is not None:
        schedule.frequencia = data.frequency
    db.session.commit()
    return {
        "Message": "Schedule updated successfully!"
    }, 200
