# 📝 Day 06 – Full CRUD Notes Manager (Flask + SQLite)

A simple Flask CRUD (Create, Read, Update, Delete) application that allows users to manage notes using a SQLite database with Flask-SQLAlchemy ORM.

This project demonstrates how to build a database-driven web application where users can:

➕ Create new notes
📖 View all saved notes
✏️ Edit existing notes
🗑️ Delete notes

---

# 📸 Project Preview

![Project Preview](assets/preview.png)

---

## 🚀 Core Concepts Covered

* **Create:** HTML Form handling via `POST` requests to save new notes in SQLite database.
* **Read:** Fetching and dynamically rendering all notes on the home page using **Jinja2** templates.
* **Update:** Dynamic Routing (`/edit/<int:id>`) to fetch existing record, pre-fill form fields, and update the database entry.
* **Delete:** Dynamic Routing (`/delete/<int:id>`) to query records via `get_or_404()` and permanently erase entries from the DB using `db.session.delete()`.

---

# 🚀 CRUD Operations

## ➕ CREATE

User submits the form.

```python
new_note = Note(title=title, content=content)

db.session.add(new_note)

db.session.commit()
```

Data is stored inside SQLite.

---

## 📖 READ

```python
all_notes = Note.query.all()
```

Fetches every record from the database.

---

## ✏️ UPDATE

Find record

```python
note = Note.query.get_or_404(id)
```

Modify values

```python
note.title = ...

note.content = ...
```

Save

```python
db.session.commit()
```

---

## 🗑️ DELETE

Find record

```python
note = Note.query.get_or_404(id)
```

Delete

```python
db.session.delete(note)

db.session.commit()
```

---

# 🌐 Dynamic Routes

Edit

```python
/edit/<int:id>
```

Delete

```python
/delete/<int:id>
```

Example

```
/edit/3
```

Here **3** is the note ID.

Flask automatically passes it to

```python
def edit_note(id):
```

---

# 🛠️ Technologies Used
Python 3
Flask
Flask-SQLAlchemy
SQLite
HTML5
CSS3

---

📁 Project Structure
Day-06-Full-CRUD-QUICKNOTES/
│
├── app.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── notes.db
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── assets/
    └── ss.png


---

# 🗃️ Database Flow

```text
HTML Form
     │
     ▼
Flask Route
     │
     ▼
SQLAlchemy Model
     │
     ▼
SQLite Database
     │
     ▼
Read Data
     │
     ▼
Jinja Template
     │
     ▼
Browser
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/noorhasann/14-Days-of-Flask-Challenge.git
```

Move into project directory

```bash
cd Day-06-Full-CRUD-Notes-Manager
```

---

## 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📦 Requirements

Example

```txt
Flask
Flask-SQLAlchemy
```

Generate automatically

```bash
pip freeze > requirements.txt
```

---

# 👨‍💻 Author

**Noor Hasan**

GitHub: https://github.com/noorhasann

Building projects while learning Flask, one day at a time.

⭐ If this project helped you learn Flask CRUD operations, consider giving the repository a star!