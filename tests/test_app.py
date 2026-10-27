from app import app


def test_index_returns_json_payload():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    payload = response.get_json()
    assert isinstance(payload, dict)
    assert payload.get("status") == "ok"
    assert "message" in payload


def test_health_returns_healthy_status():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
