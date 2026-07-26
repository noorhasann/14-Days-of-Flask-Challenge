from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------------------------------------------------
# DATABASE MODEL
# ---------------------------------------------------------
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f''

# DB Tables Creation Context
with app.app_context():
    db.create_all()

# ---------------------------------------------------------
# ROUTES
# ---------------------------------------------------------

# ⚠️ VERY IMPORTANT: Flash messages ke liye secret key mandatory hai!
app.secret_key = "super-secret-key-yahan-kuch-bhi-likho"

# 1. CREATE & READ (Home Page)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # .get() + .strip() se empty spaces wala loophole bhi band ho jata hai
        title = request.form.get('title', '').strip()
        content = request.form.get('content').strip()

        # 🛑 VALIDATION: Check agar koi bhi field khali hai
        if not title or not content:
            flash("Title aur Content dono required hain! Empty note save nahi ho sakta.", "danger")
            return redirect('/')
        
        # Naya note object bana kar DB mein save karna
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()

        # 🎉 Success Flash Message
        flash("Note successfully add ho gaya!", "success")
        return redirect('/')
    
    # Latest notes pehle dikhane ke liye order_by use kar rahe hain
    all_notes = Note.query.order_by(Note.id.desc()).all()
    return render_template('index.html', notes=all_notes)


# 2. DELETE (Dynamic Route)
@app.route('/delete/<int:id>')
def delete_note(id):
    # Dynamic Lookup: ID se note search karega ya 404 dega
    note_to_delete = Note.query.get_or_404(id)
    
    # Record delete aur commit
    db.session.delete(note_to_delete)
    db.session.commit()
    return redirect('/')


# 3. UPDATE (Edit & Save Dynamic Route)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    # Purana note DB se dhoondna
    note = Note.query.get_or_404(id)
    
    if request.method == 'POST':
        # Form submission par values overwrite karna
        note.title = request.form['title']
        note.content = request.form['content']
        
        # Overwritten data commit karna (db.session.add() ki zaroorat nahi hai)
        db.session.commit()
        return redirect('/')
    else:
        # GET request: HTML edit page par existing note bhejna (Pre-fill ke liye)
        return render_template('edit.html', note=note)

# 🚫 Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    # Returns custom 404.html along with 404 status code
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)