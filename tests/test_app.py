from app import app
import os

from flask import Flask, render_template, request, url_for

from zenpy import Zenpy


if os.path.exists("env.py"):
    import env

creds = {
    'email': os.environ.get("EMAIL"),
    'password': os.environ.get("PASSWORD"),
    'subdomain': os.environ.get("SUBDOMAIN")
}

zenpy_client = Zenpy(**creds)


def test_app():
    url = '/'
    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200


def test_ticket_viewer():
    url = '/'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

