from database import db
from models import Agendamento

# creation of a schedule

def create_schedule(data):
    new_schedule = Agendamento(
        descAgen = data.description,
        ativId = data.activity_id,
        data_hora = data.date
    )
    db.session.add(new_schedule)
    db.session.commit()
    return {"Message": "Schedule created successfully!"}

# searching for a existent schedule from a specific / will return a list of schedules linked to the specific activity

def list_schedules(data):
    schedules = db.session.execute(db.select(Agendamento).where(Agendamento.ativId == data.activity_id).order_by(Agendamento.data_hora)).scalars().all()
    schedules_list = []
    if not schedules:
        return {"Message": "Schedule not found."}
    else:
        for schedule in schedules:
            schedules_list.append({"nomeAtiv": schedule.atividade.nomeAtiv, "data_hora": schedule.data_hora, "descAgen": schedule.descAgen, 'agenId': schedule.agenId})
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
