from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_event_flow():
    payload = {"service": "axi", "user_id": "u1", "action": "login"}
    r = client.post("/events/", json=payload)
    assert r.status_code == 200
    r2 = client.get("/analytics/summary")
    assert r2.status_code == 200
    data = r2.json()
    assert "by_action" in data
    assert "login" in data["by_action"]