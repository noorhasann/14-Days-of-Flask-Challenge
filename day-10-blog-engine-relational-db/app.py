from flask import Flask, render_template, request, redirect, url_for, flash
# 1. CHANGE: BlogPost ko bhi import kiya
from models import db, User, BlogPost
# 1. NEW IMPORTS: Flask-Login utilities import kiye
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Session & Flash messages ke liye required
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)

# 2. NEW SETUP: LoginManager initialize kiya
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Unauthenticated user access kare toh kahan bhejna hai
login_manager.login_message_category = 'danger'

# 3. NEW LOADER: Flask-Login ko user dhundne ka tareeka bataya
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Database Tables Create karna (first run par)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
# Logged-in user direct dashboard jaye, baki login page par
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Agar user pehle se logged in hai, toh dobara signup na kare
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email/username already exists
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('Username or Email already taken!', 'danger')
            return redirect(url_for('signup'))

        # Create new user instance
        new_user = User(username=username, email=email)
        
        # Hash the password!
        new_user.set_password(password)

        # Save to Database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        # 4. CHANGE: Account banne ke baad ab direct login par bhejein
        return redirect(url_for('login'))

    return render_template('signup.html')

# ----------------- DAY 9 NEW ROUTES -----------------

# 5. NEW ROUTE: Login handling
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Database me username se user dhundha
        user = User.query.filter_by(username=username).first()

        # User mila AND password verify hua (`models.py` ka helper function)
        if user and user.check_password(password):
            login_user(user) # User session create ho gaya!
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# 6. NEW ROUTE: Protected Dashboard
@app.route('/dashboard')
@login_required  # Guest users is route par nahi aa sakte
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

# 7. NEW ROUTE: Logout handling
@app.route('/logout')
@login_required
def logout():
    logout_user() # User session destroy ho gaya
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# ----------------- DAY 10 NEW ROUTES -----------------

# 2. ADD: Post likhne ke liye route
@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        # current_user.id se post author ko link kar rahe hain
        new_post = BlogPost(title=title, content=content, user_id=current_user.id)
        
        db.session.add(new_post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('feed'))

    return render_template('create_post.html')

# 3. ADD: All posts & authors dekhne ke liye route
@app.route('/feed')
def feed():
    posts = BlogPost.query.all()
    return render_template('feed.html', posts=posts)

# ----------------- DELETE POST ROUTE -----------------
@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    # 1. Database se post id ke zariye dhundho (nahi milne par 404 error)
    post = BlogPost.query.get_or_404(post_id)

    # 2. Security Check: Kya ye post logged-in user ki hi hai?
    if post.author != current_user:
        flash('Aap kisi aur ki post delete nahi kar sakte!', 'danger')
        return redirect(url_for('feed'))

    # 3. Database se delete karke commit karein
    db.session.delete(post)
    db.session.commit()

    flash('Post successfully delete ho gayi!', 'success')
    return redirect(url_for('feed'))


if __name__ == '__main__':
    app.run(debug=True)