import os
import math
from flask import Flask, render_template, request, url_for

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


@app.route('/')
def ticket_viewer():
    tickets = zenpy_client.tickets()
    return render_template('index.html', tickets=tickets)


@app.route('/ticket_details/')
def ticket_details():
    return render_template('ticket_details.html')



if __name__ == '__main__':
    app.run()
