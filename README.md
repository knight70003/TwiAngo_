TwiAngo - Twitter Clone Using Django

A full-stack Twitter-inspired social media web application built using Django.
TwiAngo enables users to create, edit, delete, and search tweets with secure authentication and a clean user experience.

---

🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 📝 Create Tweets with Text & Images
- ✏️ Edit Your Tweets
- ❌ Delete Your Tweets
- 📰 Chronological Tweet Feed
- 🔎 Search Tweets by Keywords
- 👤 User-specific Tweet Management
- 📱 Responsive User Interface
- ☁️ Deployment Ready with Render

---

🛠️ Tech Stack

Backend

- Python
- Django

Frontend

- HTML5
- CSS3
- JavaScript

Database

- SQLite (Development)
- PostgreSQL (Production)

Deployment

- Render

Authentication

- Django Authentication System

---

📂 Project Structure

twiango/
├── twiango/                  # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                     # Main application
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/                # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── tweet_list.html
│   ├── tweet_form.html
│   ├── tweet_confirm_delete.html
│   ├── search_results.html
│   └── registration/
│
├── static/                   # Static assets
├── manage.py
├── requirements.txt
└── README.md

---

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone <your-repository-url>
cd twiango

---

2️⃣ Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS/Linux

python3 -m venv venv
source venv/bin/activate

---

3️⃣ Install Dependencies

pip install -r requirements.txt

---

4️⃣ Apply Database Migrations

python manage.py migrate

---

5️⃣ Run Development Server

python manage.py runserver

---

6️⃣ Open the Application

Visit:

http://127.0.0.1:8000

---

📸 Application Functionalities

🏠 Home Page

Displays the landing page and navigation system.

---

📰 Tweet Feed

View all tweets in reverse chronological order.

/tweets/

---

✍️ Create Tweet

/tweets/create/

Users can:

- Write tweet content
- Upload images
- Post tweets instantly

---

✏️ Edit Tweet

Users can edit only their own tweets.

---

❌ Delete Tweet

Users can securely delete their own tweets.

---

🔎 Search Tweets

/search/?search=<query>

Search tweets using keywords and phrases.

---

👤 User Authentication

Register

/register/

Login

/accounts/login/

Logout

/accounts/logout/

---

☁️ Deployment on Render

Step 1: Push Code to GitHub

Push your complete project to GitHub.

---

Step 2: Create Render Web Service

- Connect GitHub Repository
- Select the appropriate branch

---

Step 3: Configure Environment Variables

DATABASE_URL=your_postgresql_url
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=twiango.onrender.com

---

Step 4: Build Command

pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

---

Step 5: Start Command

gunicorn twiango.wsgi

---

🧑‍💻 Management Commands

Create Migrations

python manage.py makemigrations

Apply Migrations

python manage.py migrate

Create Superuser

python manage.py createsuperuser

Collect Static Files

python manage.py collectstatic --noinput

---

📈 Future Improvements

- ❤️ Like & Unlike Tweets
- 💬 Comment System
- 🔔 Notifications
- 👥 Follow/Unfollow Users
- 📷 Profile Pictures
- 🌙 Dark Mode
- 📱 REST API Integration
- ⚡ Real-time Chat Features

---

🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch

git checkout -b feature/your-feature

3. Commit your changes

git commit -m "Add new feature"

4. Push to GitHub

git push origin feature/y
