import requests
from flask import (
    Flask, 
    request, 
    render_template, 
    abort,
    redirect,
    jsonify
    )

# normal settings
app = Flask(__name__)

# home
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

# check resume
@app.route('/check', methods=['POST'])
def check():
    if request.method == "POST":
        return "oops!ohnoohnoohnoohno"
    else:
        return render_template("check.html")

# normal end settings
if __name__ == '__main__':
    app.run(debug=True)