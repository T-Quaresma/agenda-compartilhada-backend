# agenda-compartilhada-backend
Repositorio criado para todo desenvolvimento do backend do MVP - FullStack Basico.

Title: ShareHub

I------------------------------------------------------------------------------------------I

Project Discription

API for managing shared appointments between users.
Allows the user to create activities, add appointments and share them with other users.

I------------------------------------------------------------------------------------------I

Development tools

Python 3.14
Flask
Flask-OpenAPI3
Flask-SQLAlchemy
SQLite
Pydantic

I------------------------------------------------------------------------------------------I

Installation Instructions

Using gitbash

Make a clone of the repository:
git clone https://github.com/T-Quaresma/agenda-compartilhada-backend
go to where the backend is located:
cd agenda-compartilhada-backend

Create a virtual inviroment(venv):
py -m venv venv
source venv/scripts/activate

Install the dependencies:
pip install -r requirements.txt

Start the server:
py app.py

Checking with swagger:
http://127.0.0.1:5000/openapi

I------------------------------------------------------------------------------------------I

API functions

User

POST | Register a new user
GET | Search for a user through their name
DELETE  | Delete the user

Activity

POST | Register a new activity
GET | Search for an activity through their names
DELETE | Delete an activity

Schedule

POST | Register a new schedule to an existing activity
GET | makes an automatic list of all schedules to appear when you access an activity
DELETE | Delete a schedule

Participant

POST | Register a user to an existing activity from another user
GET | Search for registered users that are concidered participants
DELETE | Remove a participant from the activity