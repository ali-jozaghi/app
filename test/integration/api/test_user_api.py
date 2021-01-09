from fastapi.testclient import TestClient

from main import app
from src import dependencies
from src.configuration import Setting
from ..test_startup import database_info


def get_configuration():
    return Setting(
        database_username=database_info.username,
        database_password=database_info.password,
        database_host=database_info.host,
        database_port=database_info.port,
        database_name=database_info.name
    )


app.dependency_overrides[dependencies.get_configuration] = get_configuration


client = TestClient(app)


def test_create_user__given_valid_request__return_200():
    response = client.post(
        "/users",
        json={
            "fullname": "someone else",
            "email": "someone.else@mail.com"
        }
    )
    assert response.status_code == 200


def test_create_user__duplicate_email__return_400():
    response = client.post(
        "/users",
        json={
            "fullname": "someone else",
            "email": "someone1.else@mail.com"
        }
    )

    assert response.status_code == 200

    response2 = client.post(
        "/users",
        json={
            "fullname": "someone else",
            "email": "someone1.else@mail.com"
        }
    )

    assert response2.status_code == 400
    assert response2.json()["detail"] == "user with the same email is already exists."
