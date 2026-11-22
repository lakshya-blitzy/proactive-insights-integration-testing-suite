def test_health(http, base_url):
    r = http.get(f"{base_url}/health", timeout=10)
    assert r.status_code == 200

def test_projects_collection(http, base_url):
    r = http.get(f"{base_url}/projects", timeout=10)
    assert r.status_code == 200
    assert isinstance(r.json(), (list, dict))

def test_unknown_route(http, base_url):
    assert http.get(f"{base_url}/not-a-real-route", timeout=10).status_code == 404

# Gaps: auth/roles, malformed payloads, rollback, duplicate requests,
# pagination, payment callbacks and downstream-service failures.
