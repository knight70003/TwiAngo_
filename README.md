TwiAngo - Twitter Clone Project

A Django-based Twitter clone that allows users to create, edit, delete, and search tweets.

Table of Contents

Overview
Features
Tech Stack
Project Structure
Installation
Usage
Deployment
Contributing
License
Overview

Tiwango is a micro-blogging social media platform built with Django. It allows users to share thoughts (tweets), interact with other users, and explore content through search functionality.

Features

User Authentication - Register, login, and logout functionality Create Tweets - Post new tweets with text and images Edit Tweets - Modify your own tweets Delete Tweets - Remove your own tweets Tweet Feed - View all tweets in chronological order (newest first) Search - Search tweets by content User Profiles - User-specific tweet management

Tech Stack

Backend - Python, Django Database - SQLite (dev) / PostgreSQL (prod) Frontend - HTML, CSS, JavaScript Deployment - Render Authentication - Django Auth

Project Structure

twiango/
├── twiango/              # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  # Main app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── tweet_list.html
│   ├── tweet_form.html
│   ├── tweet_confirm_delete.html
│   ├── search_results.html
│   └── registration/
├── static/                # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md

Installation

Prerequisites

Python 3.8+ pip (Python package manager)

Step 1: Clone the Repository

git clone <your-repo-url> cd twiango

Step 2: Create a Virtual Environment

Windows
python -m venv venv venv\Scripts\activate

macOS/Linux
python3 -m venv venv source venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run Migrations

python manage.py migrate

Step 5: Start the Development Server

python manage.py runserver

Step 6: Access the Application

Open your browser and visit: http://127.0.0.1:8000

Usage

Home Page Visit http://127.0.0.1:8000 to see the landing page.

View All Tweets Go to http://127.0.0.1:8000/tweets/ to see all tweets.

Create a Tweet

Navigate to /tweets/create/
Fill out the tweet form
Click "Post Tweet"
Edit Your Tweet

Go to your tweet in the list
Click "Edit" on your own tweet
Modify the content
Click "Save Changes"
Delete a Tweet

Go to your tweet in the list
Click "Delete"
Confirm the deletion
User Registration

Visit /register/
Fill in username, email, and password
Click "Sign Up"
Search Tweets

Use the search bar on the site
Or visit /search/?search=<your-query>
Deployment

Deploying to Render

Push your code to GitHub

Create a new Web Service on Render

Connect your GitHub repository
Select the correct branch (usually main)
Configure Environment Variables DATABASE_URL - PostgreSQL connection string SECRET_KEY - Your Django secret key DEBUG - False ALLOWED_HOSTS - twiango.onrender.com

Set Build Command pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Set Start Command gunicorn twiango.wsgi

Deploy!
Your app will be live at https://twiango.onrender.com

Management Commands

Create migrations
python manage.py makemigrations

Apply migrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Collect static files
python manage.py collectstatic --noinput

Contributing
-Fork the repository
-Create a new branch (git checkout -b feature/your-feature)
-Commit your changes (git commit -m 'Add some feature')
-Push to the branch (git push origin feature/your-feature)
-Open a Pull Request

License
This project is open-source and available under the MIT License.


