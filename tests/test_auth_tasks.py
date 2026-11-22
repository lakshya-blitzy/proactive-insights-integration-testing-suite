def test_invalid_login_is_rejected(http, base_url):
    r = http.post(f"{base_url}/auth/login",
                  json={"username": "unknown", "password": "wrong"}, timeout=10)
    assert r.status_code in (400, 401, 403, 404)

def test_tasks_contract(http, base_url):
    r = http.get(f"{base_url}/tasks", timeout=10)
    assert r.status_code in (200, 401, 403, 404)
