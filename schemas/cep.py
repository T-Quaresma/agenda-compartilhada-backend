from pydantic import BaseModel

class CepSearch(BaseModel):
    cep: str