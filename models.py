from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuId: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    nomeUsu: Mapped[str] = mapped_column(nullable=False)
    participantesAtiv: Mapped[List["ParticipantesAtiv"]] = relationship(back_populates="usuario")

class Atividade(db.Model):
    __tablename__ = 'atividades'
    nomeAtiv: Mapped[str] = mapped_column(nullable=False)
    descAtiv: Mapped[str]
    ativId: Mapped[int] = mapped_column(primary_key=True)
    criadorId: Mapped[int] = mapped_column(ForeignKey("usuarios.usuId"))
    agendamento: Mapped[List["Agendamento"]] = relationship("Agendamento", back_populates="atividade")
    
class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    agenId: Mapped[int] = mapped_column(primary_key=True)
    descAgen: Mapped[str]
    data_hora: Mapped[datetime] = mapped_column(nullable=False)
    ativId: Mapped[int] = mapped_column(ForeignKey("atividades.ativId"))
    atividade: Mapped["Atividade"] = relationship("Atividade", back_populates="agendamento")

class ParticipantesAtiv(db.Model):
    __tablename__ = 'participantes'
    partId: Mapped[int] = mapped_column(primary_key=True)
    usuId: Mapped[int] = mapped_column(ForeignKey("usuarios.usuId"))
    agenId: Mapped[int] = mapped_column(ForeignKey("agendamentos.agenId"))
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="participantesAtiv")