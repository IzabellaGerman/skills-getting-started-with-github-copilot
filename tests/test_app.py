from urllib.parse import quote

from fastapi.testclient import TestClient

import src.app as app_module


app = app_module.app
client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity_name)}/signup?email={quote(email)}"
    )
    assert response.status_code == 200

    activity = app_module.activities[activity_name]
    assert email in activity["participants"]

    delete_response = client.delete(
        f"/activities/{quote(activity_name)}/participants/{quote(email)}"
    )
    assert delete_response.status_code == 200
    assert email not in activity["participants"]
