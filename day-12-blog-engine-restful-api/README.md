# 🚀 Day 12 — Blog RESTful API Development

A **RESTful API** built with **Flask** and **SQLAlchemy** to expose blog post data in a clean, structured JSON format.

This project is part of the **14 Days of Flask Challenge**, where each day focuses on building practical Flask concepts step by step.

---

## 📌 Day 12 Objective

The goal of Day 12 was to convert the existing Blog Engine into a **RESTful API** that can be consumed by:

* 🌐 Frontend applications
* 📱 Mobile applications
* 🖥️ Other backend services
* 🔗 Third-party clients

---

## 🧠 Core Concepts Learned

* REST API Architecture
* HTTP Methods and Status Codes
* JSON API Responses
* Database Model Serialization
* `to_dict()` Helper Method
* API Endpoint Routing
* Flask + SQLAlchemy integration
* RESTful URL structure
* API versioning using `/api/v1/`

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **SQLAlchemy**
* **SQLite**
* **JSON**
* **REST API**

---

## 📂 API Endpoints

### 1. Get All Posts

**GET**

```text
/api/v1/posts
```

Returns all blog posts in JSON format.

### Example Response

```json
{
  "posts": [
    {
      "id": 1,
      "title": "My First Blog Post",
      "content": "This is my first blog post.",
      "author_id": 1
    },
    {
      "id": 2,
      "title": "Learning Flask",
      "content": "Flask makes backend development easier.",
      "author_id": 1
    }
  ]
}
```

---

### 2. Get a Single Post

**GET**

```text
/api/v1/posts/<post_id>
```

Returns a specific blog post based on its ID.

### Example

```text
/api/v1/posts/1
```

### Example Response

```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is my first blog post.",
  "author_id": 1
}
```

If the requested post does not exist, the API returns:

```json
{
  "error": "Post not found"
}
```

with HTTP status code:

```text
404 Not Found
```

---

## 📊 HTTP Status Codes

| Status Code       | Meaning                       |
| ----------------- | ----------------------------- |
| `200 OK`          | Request successful            |
| `201 Created`     | Resource successfully created |
| `400 Bad Request` | Invalid request               |
| `404 Not Found`   | Resource does not exist       |

---

## 🔄 Model Serialization

SQLAlchemy model objects cannot be directly returned as JSON.

To solve this, a `to_dict()` helper method is used to convert database objects into Python dictionaries.

Example:

```python
def to_dict(self):
    return {
        "id": self.id,
        "title": self.title,
        "content": self.content,
        "author_id": self.author_id
    }
```

The dictionary can then be returned as a JSON response using Flask.

---

## 🏗️ API Architecture

The API follows a versioned RESTful URL structure:

```text
/api/v1/posts
```

Using API versioning makes it easier to introduce future changes without breaking existing clients.

Example:

```text
/api/v1/posts
/api/v2/posts
```

---

## 📁 Project Structure

```
Day-12/
│
├── app.py
├── models.py
├── forms.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── create_post.html
│   ├── dashboard.html
│   ├── login.html
│   ├── feed.html
│   └── signup.html
│
└── instance/
    └── blog.db

```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/noorhasann/14-Days-of-Flask-Challenge.git
```

### 2. Navigate to the Project

```bash
cd day-12-blog-engine-restful-api
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Flask Application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## 🧪 Testing the API

You can test the endpoints using:

* Browser
* Postman
* Thunder Client
* cURL

### Using cURL

Get all posts:

```bash
curl http://127.0.0.1:5000/api/v1/posts
```

Get a specific post:

```bash
curl http://127.0.0.1:5000/api/v1/posts/1
```

---

## 🎯 Learning Outcome

By completing Day 12, I learned how to:

* Build RESTful API endpoints using Flask
* Structure API URLs using versioning
* Fetch database records through SQLAlchemy
* Convert SQLAlchemy models into JSON-compatible dictionaries
* Work with HTTP status codes
* Create APIs that can be consumed by frontend and mobile applications

---

### 👨‍💻 Author

**Noor Hasan**

**GitHub:** https://github.com/noorhasann