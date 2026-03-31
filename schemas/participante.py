from pydantic import BaseModel

# ao adicionar um participante o usuario tera que clicar no agendamento especifico, selecionando o id do agendamento ao fazer isso,
# e clicar em adicionar participante, então clicar no participante da lista de pessoas na friend list dela quem ele quer adicionar.
class Participant_Addition(BaseModel):
    user_id: int
    schedule_id: int

# ao procurar por um participante só precisará procurar o nome do participante, se ele existir ele aparecera para a pessoa procurando
class Participant_Search(BaseModel):
    user_name: str
    
# Para deletar um participante o usuario ira clicar no participante especifico que ele quer e clicar em remover.
class Participant_Delete(BaseModel):
    id: int