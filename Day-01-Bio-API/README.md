# 🚀 Flask Day 1 - Basic Flask Application

A beginner-friendly Flask project created to understand the fundamentals of Flask and REST APIs.

## 📚 What I Learned

Through this project, I learned:

- Setting up a basic Flask application
- How Flask routes work
- Returning HTML responses from Flask
- Using dynamic URL parameters
- Creating a basic API endpoint
- Creating routes using `@app.route()`
- Returning JSON using `jsonify()`
- Running Flask in Debug Mode
- Understanding the basic structure of a Flask project

---

## 📂 Project Structure

```
flask-day1-app/
│── app.py
│── requirements.txt
└── README.md
```

---

## ⚙️ Features

- 🏠 Home page with HTML response
- 🔗 Dynamic URL routing (`/status/<status_msg>`)
- 📦 JSON API endpoint (`/api/profile`)
- ⚡ Debug mode enabled for development

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd flask-day1-app
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## 🌐 Available Routes

### Home

```
/
```

Returns a simple HTML page.

---

### Dynamic Status Route

```
/status/<status_message>
```

Example:

```
/status/Learning-Flask
```

Output:

```
Current Live Status:
Learning-Flask
```

---

### JSON API

```
/api/profile
```

Example Response

```json
{
    "name": "Rahul",
    "role": "Python Developer Trainee",
    "skills": [
        "Python",
        "Flask",
        "SQL"
    ],
    "is_active": true
}
```

---


## 🚀 Technologies Used

- Python
- Flask

---

## 👨‍💻 Author

**Noor Hasan**

GitHub: https://github.com/noorhasann