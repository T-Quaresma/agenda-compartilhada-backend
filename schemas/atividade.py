from pydantic import BaseModel
from typing import Optional

# User have to click on the create new activity button and fill the name, an optional description and the front will connect the 
# user to that activity
class Activity_Creation(BaseModel):
    name: str
    description: Optional[str] = None
    user_id: int

# To search an activity the user will search the activity by it's name, generating every activity with that key name to the selection list.
class Activity_Search(BaseModel):
    name: Optional[str] = None
    user_id: Optional[int] = None

# Deleting an activity the user will have to enter the activity and click the option to delete that specific activity. The front will 
# use that activity id to delete the selected one.
class Activity_Delete(BaseModel):
    activity_id: int