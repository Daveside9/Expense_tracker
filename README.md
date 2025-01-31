Expense Tracker

Description

The Expense Tracker is a web application built with Flask that allows users to track their daily expenses. Users can add, edit, and delete expenses while categorizing them for better financial management.

Features

Add new expenses with description, amount, category, and date.

View all recorded expenses on the dashboard.

Edit existing expenses.

Delete unwanted expense records.

Uses Flask and SQLite for data storage.

Technologies Used

Python (Flask)

Flask-WTF for form handling

SQLite as the database

Jinja2 for templating

HTML, CSS for frontend

Gunicorn for production deployment

Installation

Prerequisites

Ensure you have Python installed on your system. You can check by running:

python --version

If Python is not installed, download it from python.org.

Steps to Set Up Locally

Clone the repository:

git clone cd expense-tracker

Create a virtual environment:

python -m venv venv source venv/bin/activate # On macOS/Linux venv\Scripts\activate # On Windows

Install dependencies:

pip install -r requirements.txt

Initialize the database:

python

from app import db db.create_all() exit()

Run the application:

python app.py

Open your browser and go to:

http://127.0.0.1:5000

Usage

On the homepage, enter expense details and click "Add Expense."

Navigate to /dashboard to view all recorded expenses.

Edit or delete expenses as needed.

Project Structure

expense-tracker/ │── static/ │ └── app.css │── templates/ │ ├── index.html │ ├── dashboard.html │ ├── add_expense.html │ ├── edit_expense.html │── app.py │── forms.py │── requirements.txt │── README.md

API Endpoints

Endpoint

Method

Description

/

GET

Home page

/dashboard

GET

View all expenses

/add_expense

POST

Add a new expense

/edit_expense/

POST

Edit an existing expense

/delete_expense/

GET

Delete an expense

Deployment

To deploy with Gunicorn:

gunicorn -w 4 -b 0.0.0.0:5000 app:app

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch.

Commit your changes.

Push to your fork and submit a pull request.

License

This project is licensed under the MIT License.
