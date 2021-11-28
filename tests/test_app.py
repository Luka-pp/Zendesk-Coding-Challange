import os
from flask import Flask
from app import app


from zenpy import Zenpy
if os.path.exists("env.py"):
    import env


creds = {
    'email': os.environ.get("EMAIL"),
    'password': os.environ.get("PASSWORD"),
    'subdomain': os.environ.get("SUBDOMAIN")
}

zenpy_client = Zenpy(**creds)


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Zendesk Tickets'
