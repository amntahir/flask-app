import json
from app import create_app

def test_home_ok():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    payload = json.loads(resp.data)
    assert payload["status"] == "ok"
