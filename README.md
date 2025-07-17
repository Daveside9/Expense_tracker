💰 Expense Tracker
A simple, intuitive web app built with Flask and SQLite that helps you monitor daily expenses, stay organized, and manage your finances effectively.

✅ Features
Add expenses: record description, amount, category, and date.

View expenses: browse all entries on a dashboard.

Edit expenses: modify existing entries.

Delete expenses: remove unwanted records.

Categorization: organize expenses for better insights.

Flask + SQLite: lightweight, easy-to-use backend with secure storage.

Flask-WTF: robust form handling and validation.

Jinja2: dynamic HTML templating for frontend rendering.

🧱 Technologies Used
Backend: Python, Flask, Flask-WTF

Database: SQLite (via Flask SQLAlchemy or direct integration)

Frontend: HTML, CSS, Jinja2 templates

Deployment: Gunicorn (production server)

🚀 Installation
Prerequisites
Python 3.6+

pip package manager

Setup Steps
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
Create a virtual environment

bash
Copy
Edit
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Initialize the database

python
Copy
Edit
python
>>> from app import db
>>> db.create_all()
>>> exit()
Run locally

bash
Copy
Edit
python app.py
Open in browser
Visit http://127.0.0.1:5000

🧭 Usage Overview
Home (/): Add new expenses using a user-friendly form.

Dashboard (/dashboard): View, edit, or delete recorded expenses.

Add Expense (/add_expense): Handles POST requests to save new entries.

Edit Expense (/edit_expense/<id>): Edit existing records.

Delete Expense (/delete_expense/<id>): Remove entries by ID.

📁 Project Structure
php
Copy
Edit
expense-tracker/
├── static/
│   └── app.css              # Custom styling
├── templates/
│   ├── index.html           # Add-expense page
│   ├── dashboard.html       # Expense list and controls
│   ├── add_expense.html     # Add expense form
│   └── edit_expense.html    # Edit expense form
├── app.py                   # Core Flask application
├── forms.py                 # Flask-WTF form definitions
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
🚢 Deployment
Use Gunicorn for production:

bash
Copy
Edit
gunicorn -w 4 -b 0.0.0.0:5000 app:app
🤝 Contributing
Contributions welcome! To get involved:

Fork this repo.

Create a feature branch: git checkout -b feature-name

Commit changes: git commit -m "Add new feature"

Push your branch: git push origin feature-name

Open a PR and describe your changes.

📝 License
