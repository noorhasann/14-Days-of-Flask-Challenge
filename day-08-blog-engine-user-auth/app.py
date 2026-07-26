from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Session & Flash messages ke liye required
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)

# Database Tables Create karna (first run par)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Jaise hi koi 127.0.0.1:5000 par aayega, ye unhe direct /signup par bhej dega
    #this is temporary we will work on this later
    return redirect(url_for('signup'))
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
        # Abhi ke liye aisi simple string return kar rahe hain:
        return "Account created successfully! Abhi login page banna baaki hai."
        ##return redirect(url_for('login')) # jb login ban jayega

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)