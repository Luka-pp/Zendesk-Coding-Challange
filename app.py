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
    ticket_generator = zenpy_client.tickets()
    tickets = ticket_generator[0:25]
    return render_template('index.html', tickets=tickets)


@app.route('/ticket_details/<ticket_id>')
def ticket_details(ticket_id):
    ticket = zenpy_client.tickets(id=ticket_id)
    print(ticket)
    return render_template('ticket_details.html', ticket=ticket)


@app.errorhandler(404)
def handle_404(exception):
    return render_template("404_500.html", exception=exception)


@app.errorhandler(500)
def handle_500(exception):
    return render_template("404_500.html", exception=exception)


if __name__ == '__main__':
    app.run()
