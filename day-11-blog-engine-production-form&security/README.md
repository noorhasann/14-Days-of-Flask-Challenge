# 🚀 Flask Blog Engine

A modern and secure **Blog Engine** built with **Flask**, featuring user authentication, blog management, form validation, CSRF protection, and a clean responsive interface.

This project was developed as part of my **14 Days of Flask Challenge**, where each day introduces a new Flask concept while gradually building a production-style application.

---

## ✨ Features

### 👤 Authentication
- User Registration
- Secure Login & Logout
- Password Hashing using Werkzeug
- Session Management with Flask-Login

### 📝 Blog Management
- Create Blog Posts
- View Public Feed
- Author Information
- User-specific Dashboard
- Delete Own Posts
- Protected Routes

### 🛡 Security
- CSRF Protection using Flask-WTF
- Server-side Form Validation
- Secure Password Storage
- Login Required Authentication
- Authorization Checks

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | Flask |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Authentication | Flask-Login |
| Forms | Flask-WTF & WTForms |
| Password Security | Werkzeug |
| Templates | Jinja2 |
| Styling | Tailwind CSS |

---

# 📂 Project Structure

```text
day-11-blog-engine-production-form&security/
│
├── app.py                 # Main Flask application
├── models.py              # User & BlogPost models
├── forms.py               # WTForms classes
├── requirements.txt
├── instance/
│   └── blog.db
│
├── templates/
│   ├── signup.html
│   ├── login.html
│   ├── dashboard.html
│   ├── create_post.html
│   └── feed.html
│
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/noorhasann/14-Days-of-Flask-Challenge.git

cd 14-Days-of-Flask-Challenge/day-11-blog-engine
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF email-validator
```

Or install using

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 🔐 Security Features

✅ Password Hashing (Werkzeug)

✅ Flask-Login Authentication

✅ Login Required Routes

✅ CSRF Protection

✅ WTForms Validation

✅ Server-side Input Validation

✅ User Authorization

---

# 🗄 Database

The project uses **SQLite** with **SQLAlchemy ORM**.

### Models

### User

- id
- username
- email
- password_hash

### BlogPost

- id
- title
- content
- user_id (Foreign Key)

Relationship:

```
User (1)
   │
   └──────────< BlogPost (Many)
```

Each user can create multiple blog posts.

---

# 📚 Concepts Learned

- Flask Routing
- Templates (Jinja2)
- SQLAlchemy ORM
- CRUD Operations
- User Authentication
- Password Hashing
- Flask-Login
- WTForms
- CSRF Protection
- One-to-Many Relationships
- Flash Messages
- Session Management
- Authorization

---

# 🎯 Future Improvements

- Edit Blog Posts
- User Profile Page
- Rich Text Editor
- Image Upload
- Search Functionality
- Pagination
- Comments System
- Like & Bookmark Feature
- Dark Mode
- Email Verification
- Password Reset

---

# 👨‍💻 Author

**Noor Hasan**

AI & ML Engineering Student

Building projects to learn Flask, Machine Learning, and Backend Development.

GitHub:
https://github.com/noorhasann

---

# ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub.

It motivates me to keep building and sharing more open-source projects.