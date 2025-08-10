# Django CRUD Movies App 🎬

A simple Django project demonstrating **Create, Read, Update, Delete (CRUD)** operations for managing movies.  
This project is built for learning purposes — to understand how CRUD works in Django using models, forms, and views.

---

## 📌 Features
- Add new movies to the database  
- View a list of all movies  
- Update existing movie details  
- Delete movies from the database  

---

## 🛠 Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default Django DB)
- **Frontend**: HTML templates with Django Template Language

---
## 🚀 Getting Started

### 1️⃣ Clone the repository

python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Mac/Linux
source venv/bin/activate

pip install django
python manage.py migrate
python manage.py runserver 6030

Open http://localhost:6030 in your browser to view the app.

![Demo Screenshot](images/demo.png)
