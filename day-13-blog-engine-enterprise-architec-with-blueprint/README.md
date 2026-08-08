# 🚀 Day 13: Enterprise Blog Engine (Flask Blueprints Architecture)

A modular, enterprise-grade Blog Engine built with Flask, structured using the **Application Factory Pattern** (`create_app`) and **Flask Blueprints**. This project refactors a single-file Flask codebase into a scalable and clean multi-package architecture.

---

## 🚀 What I Learned

- Flask **Blueprints** for modular application design
- **Application Factory Pattern** using `create_app()`
- Clean project structure and separation of concerns
- Refactoring a monolithic Flask app into scalable modules

---

## 📁 Project Architecture

```
day-13-blog-engine-enterprise-architec-with-blueprint/
│
├── app/
│   ├── __init__.py          # Application Factory (create_app)
│   ├── extensions.py        # Centralized Extensions (SQLAlchemy, LoginManager)
│   ├── models.py            # User & BlogPost Models
│   │
│   ├── main/                # Main Blueprint (Landing & Dashboard)
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── auth/                # Auth Blueprint (Login, Signup, Logout)
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   ├── post/                # Post Blueprint (Blog CRUD & API)
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   └── templates/           # Modularized HTML Templates
│       ├── main/
│       ├── auth/
│       └── post/
│
├── README.md
├── .gitignore
├── requirements.txt         # Project Dependencies
└── run.py                   # App Entry Point
