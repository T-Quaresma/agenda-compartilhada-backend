from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date
from typing import List

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuId: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    nomeUsu: Mapped[str] = mapped_column(nullable=False)
    participantesAtiv: Mapped[List["ParticipantesAtiv"]] = relationship(back_populates="usuario")

class Grupo(db.Model):
    __tablename__ = 'grupos'
    grupoId: Mapped[int] = mapped_column(primary_key=True)
    nomeGrupo: Mapped[str] = mapped_column(nullable=False)
    criadorId: Mapped[int] = mapped_column(ForeignKey("usuarios.usuId"))
    atividades: Mapped[List["Atividade"]] = relationship("Atividade", back_populates="grupo")
    imagem: Mapped[str] = mapped_column(nullable=True)

class Atividade(db.Model):
    __tablename__ = 'atividades'
    nomeAtiv: Mapped[str] = mapped_column(nullable=False)
    descAtiv: Mapped[str]
    ativId: Mapped[int] = mapped_column(primary_key=True)
    criadorId: Mapped[int] = mapped_column(ForeignKey("usuarios.usuId"))
    agendamento: Mapped[List["Agendamento"]] = relationship("Agendamento", back_populates="atividade")
    imagem: Mapped[str] = mapped_column(nullable=True)
    grupoId: Mapped[int] = mapped_column(ForeignKey("grupos.grupoId"), nullable=True)
    grupo: Mapped["Grupo"] = relationship("Grupo", back_populates="atividades")
    
class Agendamento(db.Model):
    __tablename__ = 'agendamentos' 
    agenId: Mapped[int] = mapped_column(primary_key=True)
    nomeAgen: Mapped[str] = mapped_column(nullable=False)
    descAgen: Mapped[str] = mapped_column(nullable=True)
    ativId: Mapped[int] = mapped_column(ForeignKey("atividades.ativId"))
    atividade: Mapped["Atividade"] = relationship("Atividade", back_populates="agendamento")
    local: Mapped[str] = mapped_column(nullable=True)
    data_inicio: Mapped[date] = mapped_column(nullable=True)
    data_fim: Mapped[date] = mapped_column(nullable=True)
    hora_inicio: Mapped[time] = mapped_column(nullable=True)
    hora_fim: Mapped[time] = mapped_column(nullable=True)
    frequencia: Mapped[str] = mapped_column(nullable=True)


class ParticipantesAtiv(db.Model):
    __tablename__ = 'participantes'
    partId: Mapped[int] = mapped_column(primary_key=True)
    usuId: Mapped[int] = mapped_column(ForeignKey("usuarios.usuId"))
    agenId: Mapped[int] = mapped_column(ForeignKey("agendamentos.agenId"))
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="participantesAtiv")

