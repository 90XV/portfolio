from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/skills', methods=['GET'])
def skills():
    return render_template("skills.html")

@app.route('/fyp', methods=['GET'])
def fyp():
    return render_template("fyp.html") 

@app.route('/personal', methods=['GET'])
def personal():
    return render_template("personal.html") 

#POST STUFF
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    return render_template("personal.html")
if __name__ == '__main__':
    app.run()
