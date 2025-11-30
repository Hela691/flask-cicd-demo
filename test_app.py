from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    # on vérifie juste que le message contient "Hello from Flask"
    assert b"Hello from Flask CI/CD demo!" in resp.data
