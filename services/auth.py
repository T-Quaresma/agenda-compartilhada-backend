import requests, os

AUTH_API_URL = os.getenv(
    "AUTH_API_URL",
    "http://localhost:5001"
)

def validate_access_token(access_token):
    if not access_token:
        return None, 401

    try:
        response = requests.post(
            f"{AUTH_API_URL}/auth/validate",
            cookies={
                "access_token": access_token
            }
        )

        if response.status_code != 200:
            return None, 401

        return response.json(), 200

    except requests.RequestException:
        return None, 503