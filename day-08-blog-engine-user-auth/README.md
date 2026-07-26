# 🚀 Flask Blog Engine - Day 8: User Registration & Authentication System

Welcome to **Day 8** of building the Flask Blog Engine! Today's major milestone was implementing a secure user registration (Sign-Up) flow, password hashing using `werkzeug.security`, database integration with `Flask-SQLAlchemy`, and dynamic user feedback via Flask Flash messages.

---

## 📌 Features Implemented Today

- **User Model Schema (`models.py`)**: 
  - Defined `User` model inheriting from `db.Model` and `Flask-Login`'s `UserMixin`.
  - Added fields for `id`, unique `username`, unique `email`, and `password_hash`.
  - Implemented helper methods `set_password()` and `check_password()` for secure credential handling.

- **Backend Logic (`app.py`)**:
  - Configured Flask app with SQLAlchemy database URI (`sqlite:///blog.db`) and secret key for session management.
  - Automatic DB creation using `db.create_all()` inside application context.
  - Form data extraction (`request.form.get(...)`) and duplicate user verification (checking existing username/email).
  - Secure database insertion using `db.session.add()` and `db.session.commit()`.

- **Frontend Template (`templates/signup.html`)**:
  - Clean HTML form targeting `/signup` with POST method.
  - Jinja2 template logic to capture and render flash messages dynamically.

---

## 📁 Project Structure

```
day-08-blog-engine-user-auth/
│
├── app.py              # Main Flask application with routes and logic
├── models.py           # Database models (User schema)
├── instance/
│   └── blog.db         # SQLite database (auto-generated)
└── templates/
    └── signup.html     # Sign-up page view with Jinja2 flash messaging
```

---

# 🧠 Concepts Learned

### Database Models

Creating database tables using models.

Example fields:

* id
* username
* email
* password_hash

---

### Password Hashing

Passwords are **never stored directly**.

Instead,

```python
generate_password_hash()
```

creates a secure encrypted hash.

Example:

```
mypassword123
```

becomes something like

```
pbkdf2:sha256:600000$...
```

This protects user credentials even if the database is leaked.

---

### Password Verification

During Login (coming next),

```python
check_password_hash()
```

will compare

User Password

↓

Stored Hash

↓

Returns True / False

without ever revealing the original password.

---

### Flash Messages

Flask Flash Messages are used to display feedback.

Example:

```python
flash("Registration Successful!", "success")
```

or

```python
flash("Username already exists!", "danger")
```

Displayed inside HTML using

```jinja
get_flashed_messages()
```

---

### Redirects

Instead of rendering pages manually,

Flask redirects users using

```python
redirect(url_for("signup"))
```

This keeps URLs clean and prevents duplicate form submissions.

---

### User Validation

Before inserting a new user,

the application checks if

* username already exists
* email already exists

using

```python
User.query.filter(...)
```

This avoids duplicate accounts.

---

### Helper Methods

The User model includes helper functions.

Setting password:

```python
set_password(password)
```

Checking password:

```python
check_password(password)
```

This keeps authentication logic inside the model itself.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/noorhasann/14-Days-of-Flask-Challenge.git
```

Move inside project

```bash
cd day-08-blog-engine-user-auth
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install flask flask_sqlalchemy flask_login werkzeug
```

Run the project

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🗄️ Database Flow

```
User fills Sign Up Form
            │
            ▼
Flask receives POST Request
            │
            ▼
Validate Username & Email
            │
            ▼
Hash Password
            │
            ▼
Create User Object
            │
            ▼
Save into SQLite Database
            │
            ▼
Flash Success Message
```

---

# 🔐 Security Improvements

Implemented:

* Password Hashing
* Duplicate User Validation
* Flash Messages
* ORM (No Raw SQL)
* Secure Password Verification Method

---

# 📚 Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* Werkzeug Security
* HTML5
* Jinja2 Templates

---

# 👨‍💻 Author

**Noor Hasan**

GitHub: https://github.com/noorhasann

---

## ⭐ If you found this project helpful, don't forget to star the repository!
