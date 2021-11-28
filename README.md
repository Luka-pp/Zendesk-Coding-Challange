# Zendesk Coding Challenge

Ticket viewer application written in Python with Flask framework. This application uses **Zenpy**
wrapper for the Zendesk API interaction. Tickets layout is created by **Bootstrap**.

## Prerequisite Installations

- Python 3.9
- Flask Frameworks
- Zenpy wrapper

## Assumptions

- user has created a Zendesk account and added tickets to it
- To add a bulk of tickets from **json** format:
    - save the data from json format to **tickets.json** to your local machine
    - use the following
      command `curl https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json -v -u {email_address}:{password} -X POST -d @tickets.json -H "Content-Type:
      application/json"` where user has to insert their credentials to the fields in brackets(`{}`)

## How to run this application

- clone [THIS](https://github.com/Luka-pp/Zendesk-Coding-Challange) repository to Your local machine
- To begin user should set up following environmental variables:
    - in the root directory of your locally cloned repository create **env.py** file
    - inside env.py set up the environmental variables in the following order:
        - `os.environ.setdefault("EMAIL", "your@email.com")`
        - `os.environ.setdefault("PASSWORD", "yourpassword")`
        - `os.environ.setdefault("SUBDOMAIN", "yoursubdomain")`
- run application by `flask run` command in your editors terminal

By creating `env.py` file and setting the environmental variables inside, user is protecting their credentials for
Zendesk Login

## Usage

This application uses **Zenpy** to connect to **Zendesk API** and retrieve the tickets. Using Python/Flask application
is looping through the tickets and displaying each of them in a table. Each Ticket has a **Ticket Details** button which
redirects user to that specific ticket and all the details of that ticket are displayed. Pagination is implemented so
the user can page through the ticket in instances of 25 tickets.

## Testing

I have attempted to implement testing with Pytest. Unfortunately I did not manage to get the testing done. I have
consulted all the documentation I could find about testing my code and tried to implement it to the best of my
knowledge, but it did not work. I will continue to work on this issue until I get the automated testing implemented.

I have manually tested the application:

- All the links work as intended and redirect users to correct to expected outcome
- All the `ticket details` buttons direct user to correct ticket (I have manually compared the results to given json
  file)
- Pagination works as intended and pages through the tickets in instances of 25 tickets per page
- button on `404_500_other_errors` redirects user back to the first page oif the tickets.
- application is responsive and easy to use on all screens

## Resources

- [Zendesk Documentation](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) Authentication, help
  and pointers
- [Zenpy](http://docs.facetoe.com.au/index.html) for API connection and interaction
- [Flask](https://palletsprojects.com/p/flask/) for frameworks
- [Bootstrap](https://getbootstrap.com/) for main frame and styling
- [MDN](https://developer.mozilla.org/en-US/) general help and pointers
- [Stackoverflow](https://stackoverflow.com/) general help and pointers

### Rationale

- **Zenpy** wrapper:
    - safe and secure API interaction
    - advantage of using **Python** to write fast and clean code
    - programmatic interaction with Zendesk
    - Keeping the API calls to a minimum

- **Flask**:
    - fast and reliable framework
    - extensive documentation and examples
    - lightweight and leaves user with a lot of room for future growth

- **Bootstrap**
    - great for responsiveness
    - good performance and easy integration




