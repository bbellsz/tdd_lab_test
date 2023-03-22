from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_write_main():
    name = "Sirada"
    response = client.get("/callname",json={"name":name})
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
