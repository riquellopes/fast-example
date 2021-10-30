import pytest
import main
from fastapi.testclient import TestClient

@pytest.fixture()
def client():
    return TestClient(main.app)

def test_get_name(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Name": "Henrique Lopes"}