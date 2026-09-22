from flask_openapi3 import APIBlueprint

health_bp = APIBlueprint('health', __name__)
@health_bp.get("/health")
def health():
    return {"status": "ok"}, 200