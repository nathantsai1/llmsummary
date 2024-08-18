import requests
from flask import (
    Flask, 
    request, 
    render_template, 
    abort,
    redirect,
    jsonify
    )
# i learned how to get googleai with w3 schools
import google.generativeai as genai

# local requests
from api import api_keyed
from helpers import college

# normal settings
app = Flask(__name__)

# home
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

# check resume
@app.route('/check', methods=['POST', "GET"])
def check():
    if request.method == "POST":
        essay = request.form.get("essay")
        colleged = college(essay)
        # take api_key(hidden)
        api_key = api_keyed()
        # give api_key to genai
        genai.configure(api_key=api_key)
        # select model;
        model = genai.GenerativeModel('gemini-1.5-flash')
        # take prompt
        response = model.generate_content(colleged)
        return response.text
    else:
        return render_template("check.html")

# normal end settings
if __name__ == '__main__':
    app.run(debug=True)