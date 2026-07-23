from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (Jab tak server running hai, data list me rahega)
notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # HTML form se values collect karna
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Validation: check karein ki user ne empty fields na bheji hon
        if title and content:
            # Note ko dictionary form me list me append kar rahe hain
            notes.append({
                'title': title,
                'content': content
            })
        
        # Form submit hone ke baad URL ko refresh / clean redirect kar rahe hain
        return redirect(url_for('index'))
    
    # GET Request: Existing notes ke sath page render karna
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)