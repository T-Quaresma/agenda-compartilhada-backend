from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from database import db
from routes.usuario import bp_user
from routes.participante import bp_participant
from routes.atividade import bp_activity
from routes.agendamento import bp_schedule
from routes.grupo import bp_group
from routes.health import health_bp
from routes.cep import cep_bp



info = Info(title="Shared_Agenda API", version="1.0.0")

app = OpenAPI(__name__, info=info)
CORS(app,
     origins=["http://localhost:5173"],
     supports_credentials=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

#blueprints aqui

app.register_api(bp_user)
app.register_api(bp_participant)
app.register_api(bp_activity)
app.register_api(bp_schedule)
app.register_api(bp_group)
app.register_api(health_bp)
app.register_api(cep_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
