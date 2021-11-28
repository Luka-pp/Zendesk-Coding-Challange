import os

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
    page_size = int(request.args.get('page_size', 25))
    page = int(request.args.get('page', 1))
    try:
        ticket_generator = zenpy_client.tickets()
        total_count = ticket_generator.count

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        tickets = ticket_generator[start_index:end_index]

        return render_template('index.html',
                               tickets=tickets,
                               total_pages=total_count / page_size,
                               page=page,
                               page_size=page_size)

    except Exception as e:
        return render_template("404_500_other_errors.html", exception=e)


@app.route('/ticket_details/<ticket_id>')
def ticket_details(ticket_id):
    try:
        ticket = zenpy_client.tickets(id=ticket_id)
        return render_template('ticket_details.html', ticket=ticket)
    except Exception as e:
        return render_template("404_500_other_errors.html", exception=e)


@app.errorhandler(404)
def handle_404(exception):
    return render_template("404_500_other_errors.html", exception=exception)


@app.errorhandler(500)
def handle_500(exception):
    return render_template("404_500_other_errors.html", exception=exception)


if __name__ == '__main__':
    app.run()
