import os, pytest, requests
@pytest.fixture
def base_url():
    return os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")
@pytest.fixture
def http():
    s = requests.Session()
    yield s
    s.close()
