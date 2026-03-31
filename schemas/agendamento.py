from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Creating a Schedule for an activity the user will have to select an activity and then clicking the button to create a new squedule
# Where the user will have to fill a date and an optional discription to that schedule. The front will get the activity id to link it
# to the schedule.
class Schedule_Creation(BaseModel):
    description: Optional[str] = None
    date: datetime
    activity_id: int

# to search a schedule within an activity the user will have to access the activity in question and the schedules will automaticaly show up.

class Schedule_Search(BaseModel):
    activity_id: int

# Deleting a schedule the user have to select the specific Schedule and clicking the delete option to it. the front will use the activity id 
# tied to it to delete that specific schedule.
class Schedule_Delete(BaseModel):
    schedule_id: int