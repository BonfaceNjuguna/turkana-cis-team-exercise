def test_health_reports_database_and_places(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["places"] == 11


def test_unknown_address_is_404(client):
    assert client.get("/api/does-not-exist").status_code == 404
