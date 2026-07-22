from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    # Dynamic list pass kar sakte hain
    project_list = [
        {"title": "Flask Portfolio", "tech": "Python, Flask, HTML/CSS"},
        {"title": "Weather App", "tech": "Python, API, Jinja2"},
    ]
    return render_template('projects.html', projects=project_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)