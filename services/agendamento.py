from database import db
from models import Agendamento

# creation of a schedule

def create_schedule(data):
    new_schedule = Agendamento(
        nomeAgen = data.name,
        descAgen = data.description,
        ativId = data.activity_id,
        local = data.local,
        data_inicio = data.starting_date,
        data_fim = data.ending_date,
        hora_inicio = data.starting_time,
        hora_fim = data.ending_time,
        frequencia = data.frequency
    )
    db.session.add(new_schedule)
    db.session.commit()
    return {"Message": "Schedule created successfully!", "agenId": new_schedule.agenId}

# searching for a existent schedule from a specific / will return a list of schedules linked to the specific activity

def list_schedules(data):
    query = db.select(Agendamento)
    if data.activity_id:
        query = query.where(Agendamento.ativId == data.activity_id)
    if data.agenId:
        query = query.where(Agendamento.agenId == data.agenId)
    query = query.order_by(Agendamento.data_inicio, Agendamento.hora_inicio)
    schedules = db.session.execute(query).scalars().all()
    schedules_list = []
    if not schedules:
        return []
    else:
        for schedule in schedules:
            schedules_list.append({"nomeAtiv": schedule.atividade.nomeAtiv, "ativId": schedule.ativId, "nomeAgen": schedule.nomeAgen, "data_inicio": schedule.data_inicio, "hora_inicio": str(schedule.hora_inicio) if schedule.hora_inicio else None,
                                    "data_fim": schedule.data_fim, "hora_fim": str(schedule.hora_fim) if schedule.hora_fim else None, "frequencia": schedule.frequencia, "local": schedule.local, "descAgen": schedule.descAgen,
                                    'agenId': schedule.agenId})
        return schedules_list
        
    
# Deleting an existing schedule
    
def delete_schedule(data):
    schedule = db.session.execute(db.select(Agendamento).where(Agendamento.agenId == data.schedule_id)).scalars().first()
    if schedule is None:
        return {"Message": "No schedules were created for that time."}
    else: 
        db.session.delete(schedule)
        db.session.commit()
        return {"Message": "Schedule deleted Successfully."}
    
# Deleting all schedules from a specific activity
    
def delete_all_schedules(data):
    schedules = db.session.execute(db.select(Agendamento).where(Agendamento.ativId == data.activity_id)).scalars().all()
    if not schedules:
        return {"Message": "This activity have no schedules at this time."}
    else:
        for schedule in schedules:
            db.session.delete(schedule)
        db.session.commit()
        return {"Message": "All schedules deleted successfully."}
    
def update_schedule(data):
    schedule = db.session.execute(db.select(Agendamento).where(Agendamento.agenId == data.schedule_id)).scalars().first()
    if not schedule:
        return {"Message": "Schedule could not be updated."}
    else:
        if data.name:
            schedule.nomeAgen = data.name
        if data.description:
            schedule.descAgen = data.description
        if data.local:
            schedule.local = data.local
        if data.starting_date:
            schedule.data_inicio = data.starting_date
        if data.ending_date:
            schedule.data_fim = data.ending_date
        if data.starting_time:
            schedule.hora_inicio = data.starting_time
        if data.ending_time:
            schedule.hora_fim = data.ending_time
        if data.frequency:
            schedule.frequencia = data.frequency
        db.session.commit()
        return {"Message": "Schedule updated sucessfully!"}
