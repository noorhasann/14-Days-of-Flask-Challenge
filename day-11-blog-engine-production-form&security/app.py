from flask import Flask, render_template, redirect, url_for, flash
from models import db, User, BlogPost
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# --- DAY 11 NEW IMPORT ---
from forms import SignupForm, LoginForm, PostForm

app = Flask(__name__)
# CSRF protection ke liye Secret Key hona zaroori hai
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('signup'))
    
# --- DAY 11 UPDATED: SIGNUP ROUTE ---
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = SignupForm()  # 1. Form Instance Banaya
    
    # 2. validate_on_submit() check karega POST method + validators (Length, Email, DataRequired)
    if form.validate_on_submit():
        # Form values ko 'form.field.data' se read karte hain
        existing_user = User.query.filter(
            (User.email == form.email.data) | (User.username == form.username.data)
        ).first()
        
        if existing_user:
            flash('Username or Email already taken!', 'danger')
            return redirect(url_for('signup'))

        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form) # 3. Form template me pass kar diya

# --- DAY 11 UPDATED: LOGIN ROUTE ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm() # 1. Form Instance
    
    if form.validate_on_submit(): # 2. Automatically checks CSRF & Validations
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# --- DAY 11 UPDATED: CREATE POST ROUTE ---
@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm() # 1. Form Instance
    
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data, 
            content=form.content.data, 
            user_id=current_user.id
        )
        
        db.session.add(new_post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('feed'))

    return render_template('create_post.html', form=form)

@app.route('/feed')
def feed():
    posts = BlogPost.query.all()
    return render_template('feed.html', posts=posts)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    if post.author != current_user:
        flash('Aap kisi aur ki post delete nahi kar sakte!', 'danger')
        return redirect(url_for('feed'))

    db.session.delete(post)
    db.session.commit()

    flash('Post successfully delete ho gayi!', 'success')
    return redirect(url_for('feed'))

if __name__ == '__main__':
    app.run(debug=True)