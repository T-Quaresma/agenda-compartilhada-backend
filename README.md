# agenda-compartilhada-backend (SHARP)

Repositorio criado para o desenvolvimento da API principal do projeto SHARP - MVP Full Stack.

## Title: SHARP

I------------------------------------------------------------------------------------------I

## Project Description

API for managing shared activities and schedules between users.

Allows users to create activities, add schedules and share them with other users through participants.
Activities can be organized into groups, and schedules support date, time, location and frequency settings.

The API uses the SHARP Authentication API for authentication and authorization and communicates with the ViaCEP external API to retrieve address information from Brazilian postal codes.

I------------------------------------------------------------------------------------------I

## Development Tools

Python 3.14
Flask
Flask-OpenAPI3
Flask-SQLAlchemy
Flask-CORS
SQLite
Pydantic
Requests
Werkzeug
Docker

I------------------------------------------------------------------------------------------I

## Project Architecture

SHARP is composed of three developed components and one external API:

**Frontend**
- React and TypeScript application.
- Runs on port 5173.
- Communicates with the Principal API and Authentication API.

**Principal API**
- Python and Flask REST API.
- Runs on port 5000.
- Manages users, groups, activities, schedules and participants.
- Stores application data using SQLite.
- Communicates with the Authentication API to validate authenticated requests.
- Communicates with ViaCEP to retrieve address information.

**Authentication API**
- Python and Flask REST API.
- Runs on port 5001.
- Responsible for registration, login, JWT validation, token refresh and logout.
- Communicates with the Principal API to register users and verify credentials.

**External API**
- ViaCEP.
- Used to retrieve address information from Brazilian postal codes.

## Project Architecture

The following diagram illustrates the architecture and communication between the components of the Sharp application:

![Sharp Architecture Diagram](/docs/sharp-architecture.png)

I------------------------------------------------------------------------------------------I

## Local Installation

These instructions can be used to execute the Principal API locally without Docker.

**Prerequisites**

Python 3.14
pip
Git

The SHARP Authentication API must also be running on port 5001 for authenticated routes to work.

**Using Git Bash**

**1. Clone the repository:**

git clone https://github.com/T-Quaresma/agenda-compartilhada-backend

**2. Go to the project directory:**

cd agenda-compartilhada-backend

**3. Create a virtual environment:**

py -m venv venv

**4. Activate the virtual environment:**

source venv/Scripts/activate

**5. Install the dependencies:**

pip install -r requirements.txt

**6. Start the Principal API:**

py app.py

**The Principal API will be available at:**

http://localhost:5000

**Swagger documentation will be available at:**

http://localhost:5000/openapi/swagger

The SQLite database is created automatically by the application.

I------------------------------------------------------------------------------------------I

## Docker Execution

The Principal API can also be executed inside a Docker container.

**Prerequisites**

Docker Desktop must be installed and running.

The Authentication API must also be available for authenticated routes to work.

**1. Clone the repository:**

git clone https://github.com/T-Quaresma/agenda-compartilhada-backend

**2. Enter the project directory:**

cd agenda-compartilhada-backend

**3. Build the Docker image:**

docker build -t sharp-principal .

**4. Create the Docker network used by the SHARP APIs:**

docker network create sharp-network

The Principal API and Authentication API use this network to communicate with each other through their container names.

If the network already exists, it does not need to be created again.

**5. Create a Docker volume for the SQLite database:**

docker volume create sharp-database

This volume keeps the SQLite database even if the Principal API container is stopped or removed.

**6. Start the Principal API container:**

Using Git Bash on Windows:

MSYS_NO_PATHCONV=1 docker run -d --name sharp-principal \
  --network sharp-network \
  -p 5000:5000 \
  -e AUTH_API_URL=http://sharp-auth:5001 \
  -v sharp-database:/app/instance \
  sharp-principal

**The parameters used in this command are:**

--name sharp-principal  
Defines the name of the container.

--network sharp-network  
Connects the container to the SHARP Docker network.

-p 5000:5000  
Makes the Principal API available through port 5000.

-e AUTH_API_URL=http://sharp-auth:5001  
Defines the address used by the Principal API to communicate with the Authentication API.

-v sharp-database:/app/instance  
Stores the SQLite database inside the persistent Docker volume.

**The Principal API will be available at:**

http://localhost:5000

**Swagger documentation will be available at:**

http://localhost:5000/openapi/swagger

**Important:**

The Authentication API container must be connected to the same `sharp-network` network and must use the container name `sharp-auth`.

The instructions for executing the Authentication API are available in its own repository.

I------------------------------------------------------------------------------------------I

## Docker Commands

**To view running containers:**

docker ps

**To view all containers:**

docker ps -a

**To view Docker images:**

docker images

**To stop the Principal API:**

docker stop sharp-principal

**To start the existing Principal API container again:**

docker start sharp-principal

**To stop and remove the Principal API container:**

docker stop sharp-principal

docker rm sharp-principal

Removing the container does not remove the SQLite data stored in the `sharp-database` Docker volume.

I------------------------------------------------------------------------------------------I

## Authentication and Authorization

Protected routes require a valid authentication session.

The Principal API receives the access token through an HTTP-only cookie and sends it to the SHARP Authentication API for validation.

After validation, the authenticated user information is used to control access to groups, activities, schedules and participants.

Users can only modify resources that belong to them.

I------------------------------------------------------------------------------------------I

## API Functions

**User**

POST | Register a new user  
GET | Search for a user through their name  
DELETE | Delete a user

**Authentication**

POST | Verify user email and password for the Authentication API

**Group**

POST | Register a new activity group with optional avatar  
GET | Search for groups belonging to the authenticated user  
PUT | Update a group name and avatar  
DELETE | Delete a group and its related activities, schedules and participants

**Activity**

POST | Register a new activity linked to the authenticated user and optionally to a group  
GET | Search for activities belonging to the authenticated user by name, activity id or group id  
PUT | Update an activity name, description, image and group  
DELETE | Delete an activity and its related schedules and participants

**Schedule**

POST | Register a new schedule linked to an existing activity, with name, description, start and end date, start and end time, location and frequency  
GET | Search for schedules belonging to activities owned by the authenticated user  
PUT | Update schedule fields  
DELETE | Delete a schedule and its related participants

**Participant**

POST | Add a user as a participant to an existing schedule  
GET | Search for participants registered in a schedule  
DELETE | Remove a participant from a schedule

**CEP**

GET | Search for address information using a Brazilian CEP through the ViaCEP external API


I------------------------------------------------------------------------------------------I

## External API

The SHARP Principal API integrates with ViaCEP to retrieve address information from Brazilian postal codes.

The CEP route receives an 8-digit CEP and sends a request to ViaCEP.

**The data returned by ViaCEP is processed by the Principal API and returns:**

- Street
- Neighborhood
- City
- State

The frontend uses this information to help fill the location field when creating or editing schedules.

I------------------------------------------------------------------------------------------I

## Database

The application uses SQLite for data persistence.

**Main entities:**

Usuario  
Grupo  
Atividade  
Agendamento  
ParticipantesAtiv

**Relationship structure:**

Usuario
  |
  +-- Grupo
       |
       +-- Atividade
            |
            +-- Agendamento
                 |
                 +-- ParticipantesAtiv

Deleting a group also deletes its related activities, schedules and participants.

Deleting an activity also deletes its related schedules and participants.

Deleting a schedule also deletes its related participants.

When executed with Docker, the SQLite database is stored in the `sharp-database` Docker volume, allowing the data to persist even if the Principal API container is removed.