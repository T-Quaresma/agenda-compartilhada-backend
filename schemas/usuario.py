from pydantic import BaseModel

# para a criação de um usuario, ele tera que cadastrar um nome, uma senha e um email a essa conta.
class User_Creation(BaseModel):
    name: str
    senha: str
    email: str

# para procurar um usuario o usuario tera que escrever o nome desse usuario aparecendo todas as opçoes disponiveis, assim como 
#procurar um usuario no whatsapp.
class User_Search(BaseModel):
    name: str

    
# para deletar o sua propria conta o usuario tera que clicar na opção deletar conta, onde o front vai pegar o id dessa conta e deleta-la
class User_Delete(BaseModel):
    id: int

