from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Aapka dynamic data (Dictionary)
    user_data = {
        "name": "Noor Hasan",
        "bio": "Passionate Developer | Learning Flask & Web Dev",
        "skills": ["Python", "Flask", "HTML/CSS", "Jinja2", "Git"],
        "projects": [
            {
                "title": "Day 1 Mini-Project",
                "description": "Basic Flask Setup & Routing Example",
                "link": "#"
            },
            {
                "title": "Day 2 Mini-Project",
                "description": "Dynamic Bio & Interactive Portfolio",
                "link": "#"
            }
        ],
        "socials": {
            "GitHub": "https://github.com/noorhasann",
            "LinkedIn": "https://www.linkedin.com/in/noorhasan123",
            "Twitter": "https://twitter.com"
        }
    }
    # Jinja template ko data ke sath render kar rahe hain
    return render_template("index.html", profile=user_data)

if __name__ == "__main__":
    app.run(debug=True)