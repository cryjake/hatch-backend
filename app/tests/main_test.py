import unittest
from fastapi.testclient import TestClient
from mockfirestore import MockFirestore

from ..main import app
from datetime import datetime

app.db = MockFirestore()
client = TestClient(app)

token = {
    'uid': "tester"
}


def test_create_user_no_token():
    response = client.post(
        "/create_user",
        json={
            "username": "Ed",
            "name": {
                "first": "Edson",
                "last": "Shivuri"
            },
            "dob": datetime.now(),
            "userType": "user",
            "gender": "male"

        }
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Missing Access Token"}


def test_create_user_success():
    response = client.post(
        "/create_user",
        headers={
            "Access-Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJjOGUyYjI5NmM2ZjMyODRlYzMwYjg4NjVkNzI5M2U2MjdmYTJiOGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaGF0Y2gtdHYtbW9iaWxlLWFwcCIsImF1ZCI6ImhhdGNoLXR2LW1vYmlsZS1hcHAiLCJhdXRoX3RpbWUiOjE2MTkwMDM3ODQsInVzZXJfaWQiOiJvWGs5dUFsMjA1WVQ0ZXhOYUw4MXk5aUFDdjMzIiwic3ViIjoib1hrOXVBbDIwNVlUNGV4TmFMODF5OWlBQ3YzMyIsImlhdCI6MTYxOTAwMzc4NCwiZXhwIjoxNjE5MDA3Mzg0LCJlbWFpbCI6ImVkc29uMTBAdGVzdC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZWRzb24xMEB0ZXN0LmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.RrHfiERyOhlLkMTM5UNQVb71l94j2fzoJwxnfQU6e_KGqeqWuchzAME-Fzm_SFKyVyhcP6d8_kAGdNSxBbIwVDVfEcoRi-H1tvjyWjkXioxmuhKjbyKCuMOwyZRR4Y_CHrr158V5dhIM5vhk1wDBP8ToPgVURyO3buud0TNABXWheXHqxmxzXcVs9q80R3lBE6ItzNsoFfKy1TW3qPr8KDn6Rt_5TucJeFbUazR8VmbhtSovehuZHAUBFJ-4gDPfC3QlZk6l58308KBGehbSWnHruFyVo-7RefTQKPkMv-aHwwdIJpfWwUXaN7U9GUZbG4Sx4jpHaeFxXT3UHyIkZg"},
        json={
            "username": "Ed",
            "name": {
                "first": "Edson",
                "last": "Shivuri"
            },
            "dob": datetime.now(),
            "userType": "user",
            "gender": "male"

        }
    )

    assert response.status_code == 201
    assert response.json() == {
        "bio": None,
        "dob": "1619003907",
        "username": "Ed",
        "gender": "male",
        "location": None,
        "phone": None,
        "name": {
            "last": "Shivuri",
            "first": "Edson"
        },
        "userType": "user",
        "displayImage": None    }
