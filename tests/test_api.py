from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_recommend():
    response = client.get("/recommend/1")
    assert response.status_code == 200
    assert "results" in response.json()


def test_invalid_user():
    response = client.get("/recommend/9999")
    assert response.status_code in [200, 404]