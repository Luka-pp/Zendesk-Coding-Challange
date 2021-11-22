import os
from flask import Flask

from zenpy import Zenpy

app = Flask(__name__)
if os.path.exists("env.py"):
    import env


creds = {
    'email': os.environ.get("EMAIL"),
    'password': os.environ.get("PASSWORD"),
    'subdomain': os.environ.get("SUBDOMAIN")
}

zenpy_client = Zenpy(**creds)


for ticket in zenpy_client.search(type='ticket'):
    print(ticket.requester.name)
    print(ticket.to_json())


if __name__ == '__main__':
    app.run()
