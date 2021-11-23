import os
from flask import Flask, render_template

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
def ticket():
    tickets = zenpy_client.search(type='ticket')
    return render_template('index.html', tickets=tickets)


#for ticket in zenpy_client.search(type='ticket'):
#    print(ticket.requester.name)
#    print(ticket.to_json())
#for user in zenpy_client.users():
#    print(user.name)


if __name__ == '__main__':
    app.run()
