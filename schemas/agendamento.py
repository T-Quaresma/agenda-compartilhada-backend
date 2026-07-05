from pydantic import BaseModel
from datetime import date, time
from typing import Optional

# Creating a Schedule for an activity the user will have to select an activity and then clicking the button to create a new schuedule
# Where the user will have to fill a date and an optional discription to that schedule. The front will get the activity id to link it
# to the schedule.
class Schedule_Creation(BaseModel):
    name: str
    description: Optional[str] = None
    starting_date: Optional[date] = None
    ending_date: Optional[date] = None
    starting_time: Optional[time] = None
    ending_time: Optional[time] = None
    frequency: Optional[str] = None
    local: Optional[str] = None
    activity_id: int

# to search a schedule within an activity the user will have to access the activity in question and the schedules will automaticaly show up.

class Schedule_Search(BaseModel):
    activity_id: Optional[int] = None
    agenId: Optional[int] = None

# Deleting a schedule the user have to select the specific Schedule and clicking the delete option to it. the front will use the activity id 
# tied to it to delete that specific schedule.
class Schedule_Delete(BaseModel):
    schedule_id: int

class Schedule_Update(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    starting_date: Optional[date] = None
    ending_date: Optional[date] = None
    starting_time: Optional[time] = None
    ending_time: Optional[time] = None
    frequency: Optional[str] = None
    local: Optional[str] = None
    schedule_id: int