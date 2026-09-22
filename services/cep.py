import requests

def cep_search(cep_data):
    if not cep_data.cep.isdigit() or len(cep_data.cep) != 8:
        return {"Message": "CEP must have 8 digits."}, 400
    response = requests.get(f"https://viacep.com.br/ws/{cep_data.cep}/json/")
    data = response.json()
    if data.get("erro"):
        return {"Message": "CEP not found."}, 404
    result = {
        "rua": data.get("logradouro"),
        "bairro": data.get("bairro"),
        "cidade": data.get("localidade"),
        "estado": data.get("uf")
    }   
    return result, response.status_code