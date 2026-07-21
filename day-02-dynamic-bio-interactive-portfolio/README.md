# 🚀 Dynamic Bio & Interactive Portfolio

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Jinja2](https://img.shields.io/badge/Jinja2-Template%20Engine-red)
![Status](https://img.shields.io/badge/Challenge-Day%202-success)
![License](https://img.shields.io/badge/License-MIT-green)

A dynamic, light-weight personal portfolio website built with **Python**, **Flask**, and **Jinja2**.

This project was built as part of my **Day 2 Mini-Project** in Web Development, focusing on rendering dynamic UI components using backend data structures instead of hardcoded HTML.

---

# 📷 Preview

```
(assets/ss.png)
```

---

# 🎯 What I Learned

- Rendering HTML using `render_template()`
- Passing Python dictionaries to HTML
- Passing Python lists to HTML
- Using Jinja2 variables
- Using Jinja2 loops (`for`)
- Using Jinja2 conditions (`if`)

---

# 📁 Project Structure

```
Day-02-my-portfolio/
│
├── app.py
├── templates/
│   └── index.html
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Day-2-my-portfolio.git
```

### Go inside project

```bash
cd Day-2-my-portfolio
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Flask

```bash
pip install flask
```

### Run the Project

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🧠 Understanding the Code

## Step 1

Create a Flask app

```python
app = Flask(__name__)
```

This creates the Flask application.

---

## Step 2

Define a Route

```python
@app.route("/")
```

Whenever someone visits

```
/
```

the `home()` function executes.

---

## Step 3

Store Data in Python

```python
user_data = {
    ...
}
```

Instead of writing information inside HTML, everything is stored in a Python dictionary.

This makes the webpage dynamic.

---

## Step 4

Pass Data to HTML

```python
return render_template(
    "index.html",
    profile=user_data
)
```

The dictionary is sent to the HTML template using the variable:

```
profile
```

Now HTML can access every value.

Example:

```html
{{ profile.name }}
```

Output:

```
Noor Hasan
```

---

# 🌟 Jinja2 Basics Used

## Variables

```html
{{ profile.name }}
```

Displays the value of a variable.

---

## If Statement

```html
{% if profile.skills %}
```

Checks whether the skills list exists.

---

## For Loop

```html
{% for skill in profile.skills %}
```

Loops through every skill.

Example output:

```
Python
Flask
HTML/CSS
Git
```

---

## Dictionary Iteration

```html
{% for platform, link in profile.socials.items() %}
```

Loops through every social media link.

Output:

```
GitHub
LinkedIn
Twitter
```

---

# 💡 Key Takeaway

Instead of hardcoding data inside HTML, Flask allows us to generate dynamic webpages by passing Python objects (lists, dictionaries, etc.) to Jinja2 templates.

This separation of backend logic and frontend presentation makes applications easier to maintain and scale.

---

# 🛠️ Tech Stack

- Python
- Flask
- Jinja2
- HTML5
- CSS3

---

# 👨‍💻 Author

**Noor Hasan**

GitHub:
https://github.com/noorhasann

---

## ⭐ If you found this project helpful

Give this repository a **Star ⭐**

It motivates me to continue my **14 Days of Flask Challenge** 🚀