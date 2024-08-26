import pytest
from fastapi.testclient import TestClient
from app.db.connection import init_db
from main import app


@pytest.fixture(autouse=True)
async def initialize_test_database():
    yield await init_db()


@pytest.fixture
def client():
    return TestClient(app)


def test_create_dummy(client):
    with TestClient(app) as client:
        response = client.post("/test", json={"test": "test"})
        assert response.status_code == 200
        assert response.json()["test"] == "test"


def test_delete_dummy(client):
    with TestClient(app) as client:
        # add entry
        response = client.post("/test", json={"test": "test"})
        test_id = response.json()["_id"]

        # delete entry
        delete_response = client.delete("/test/" + test_id)
        assert delete_response.status_code == 200
        assert delete_response.json()["message"] == "Dummy deleted"
