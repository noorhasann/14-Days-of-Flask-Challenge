from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # 1. ADD: User -> BlogPosts relationship
    # 1-to-Many Relationship: Links User to BlogPost
    # 'author' allows you to access `post.author` to get the User object
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    # Helper method to set hashed password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Helper method to verify password during login
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 2. ADD: BlogPost Model
class BlogPost(db.Model):
    __tablename__ = 'blog_post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key pointing to user.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)