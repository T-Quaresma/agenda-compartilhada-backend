from flask_openapi3 import APIBlueprint
from schemas.cep import CepSearch
from tags import cep_tag
from services.cep import cep_search

cep_bp = APIBlueprint("cep", __name__)

@cep_bp.get('/cep', tags=[cep_tag])
def search_cep(query: CepSearch):
    try:
        result, status = cep_search(query)
        return result, status
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"Message": "Error searching CEP."}, 500



