from linux_package_index.app import app
from fastapi.testclient import TestClient


client = TestClient(app)

# Add package
def test_add_package():
    package = {
        "name": "Spotify",
        "website": "https://www.spotify.com/download/linux/",
        "deb": None,
        "rpm": None,
    }
    response = client.post("/packages", json=package)
    assert response.status_code == 200
    json = response.json()
    assert json["name"] == package["name"]
    assert json["website"] == package["website"]
    assert json["deb"] == package["deb"]
    assert json["rpm"] == package["rpm"]
