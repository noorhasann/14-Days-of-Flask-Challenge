from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# SQLite Database setup (instance folder me quicknotes.db file banegi)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quicknotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODEL ---
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.id} - {self.title}>'

# App start hone se pehle Database & Tables create karna
with app.app_context():
    db.create_all()

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Form se data extract karna
        note_title = request.form['title']
        note_content = request.form['content']
        
        # New Note Model Instance create karna
        new_note = Note(title=note_title, content=note_content)
        
        # Database me record add & commit karna
        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Database error: {e}"

    # Persistent Notes retrieve karna (Newest pehle dikhane ke liye)
    notes = Note.query.order_by(Note.date_created.desc()).all()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)