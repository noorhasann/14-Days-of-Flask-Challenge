from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Sample profile data
USER_PROFILE = {
    "name": "Rahul",
    "role": "Python Developer Trainee",
    "skills": ["Python", "Flask", "SQL"],
    "is_active": True
}


@app.route("/")
def home():
    """
    Home page of the application.
    Returns a simple HTML response.
    """
    return """
    <h1>🚀 Welcome to My Day 1 Flask App!</h1>
    <p>Learning Flask one step at a time.</p>

    <h3>Available Routes</h3>
    <ul>
        <li><a href="/api/profile">Profile API</a></li>
        <li><a href="/status/Learning-Flask">Sample Status Route</a></li>
    </ul>
    """


@app.route("/status/<string:status_msg>")
def update_status(status_msg):
    """
    Displays a dynamic status message.
    """
    return f"""
    <h2>📢 Current Status</h2>
    <p>{status_msg}</p>
    """


@app.route("/api/profile")
def get_profile():
    """
    Returns sample profile data as JSON.
    """
    return jsonify(USER_PROFILE)


if __name__ == "__main__":
    app.run(debug=True)