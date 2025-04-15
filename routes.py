from __main__ import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/profile', methods=['GET'])
def profile():
    return render_template("profile.html")