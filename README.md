# agenda-compartilhada-backend
Repositorio criado para todo desenvolvimento do backend do MVP - FullStack Basico.

Title: ShareHub

I------------------------------------------------------------------------------------------I

Project Discription

API for managing shared appointments between users.
Allows the user to create activities, add schedules and share them with other users.
Activities can be organized into groups, and schedules support date, time, location and frequency settings.

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
DELETE | Delete the user

Group

POST | Register a new activity group with optional avatar
GET | Search for groups by user or group id
PUT | Update a group name and avatar
DELETE | Delete a group (does not delete activities inside it)

Activity

POST | Register a new activity linked to a user and optionally to a group
GET | Search for an activity by name, user id, activity id or group id
PUT | Update an activity name, description, image and group
DELETE | Delete an activity

Schedule

POST | Register a new schedule linked to an existing activity, with name, description, start and end date, start and end time, location and frequency
GET | Search for schedules by activity id or schedule id
PUT | Update a schedule fields
DELETE | Delete a schedule

Participant

POST | Register a user to an existing activity from another user
GET | Search for registered users that are considered participants
DELETE | Remove a participant from the activity
