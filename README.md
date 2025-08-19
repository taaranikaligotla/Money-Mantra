# Money Mantra

Money Mantra is a web application designed to help you track expenses, manage budgets, and generate insightful reports. Built with Python and Flask, it offers a user-friendly interface to keep your finances in check.

# Features

- Expense Tracking: Log and categorize your expenses effortlessly.
- Budget Management: Set and monitor budgets to stay on track.
- Reports: Generate detailed reports to analyze your spending habits.
- User Authentication: Secure login and registration system.
- Responsive Design: Access your finances on any device.

# Getting Started
Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- PostgreSQL (for database management)

Installation
- Clone the repository:
- git clone https://github.com/taaranikaligotla/Money-Mantra.git
- cd Money-Mantra
- Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
- Install dependencies:
```
 pip install -r requirements.txt
```
- Set up the database:
```
psql -U postgres -f dbCreateStatements-Postgres.txt
```
- Configure environment variables:

Create a .env file and add your PostgreSQL credentials:
```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=money_mantra
```

- Run the application:
```
python app.py
```

- The app will be live at http://localhost:5000.

# Testing

Run the test suite to ensure everything is functioning correctly:
'''
pytest
'''

# Live Demo

The app is deployed on Render! Access it here:
Money Mantra Live: https://money-mantra.onrender.com/


