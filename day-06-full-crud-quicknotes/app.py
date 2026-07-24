from flask import Flask, render_template, request, redirect
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

# 1. CREATE & READ (Home Page)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Form se dynamic data pakdna
        title = request.form['title']
        content = request.form['content']
        
        # Naya note object bana kar DB mein save karna
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect('/')
    
    # READ: DB se saare notes mangwana
    all_notes = Note.query.all()
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


if __name__ == '__main__':
    app.run(debug=True)