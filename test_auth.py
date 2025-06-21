from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_flow():
    client.post("/auth/register", data={"username":"bob","password":"secret"})
    res = client.post("/auth/login", data={"username":"bob","password":"secret"})
    assert res.status_code == 200
    token = res.json()["access_token"]
    assert token
    res2 = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert res2.status_code == 200