import requests
from flask import (
    Flask, 
    request, 
    render_template, 
    abort,
    redirect,
    jsonify
    )
import json
# i learned how to get googleai with w3 schools
import google.generativeai as genai

# local requests
from api import api_keyed
from helpers import college, reads

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
        try:
            essay = request.form.get("essay")
        except ValueError:
            return redirect('/check')
        colleged = college(essay)
        # take api_key(hidden)
        api_key = api_keyed()
        # give api_key to genai
        genai.configure(api_key=api_key)
        # select model;
        model = genai.GenerativeModel('gemini-1.5-flash')
        # take prompt
        mesponse = model.generate_content(colleged)

        # get information from json
        alread = reads(mesponse.text)
        hi = alread[0]
        try:
            jsoned = json.loads(fr'{hi}')
        except TypeError:
            return render_template('404.html')

        # and sort it
        # by reviews(numbers)
        # return jsonify(jsoned)
        j1 = jsoned["1"][0]
        j2 = jsoned["2"][0]
        j3 = jsoned["3"][0]
        j4 = jsoned["4"][0]

        # and strings
        js1 = jsoned["1"]
        js2 = jsoned["2"]
        js3 = jsoned["3"]
        js4 = jsoned["4"]

        js1 = js1[4:]
        js2 = js2[4:]
        js3 = js3[4:]
        js4 = js4[4:]

        # make json(1 = string, 1r = rating)
        dictionary = {"1": js1, "1r": j1, "2": js2, "2r": j2, "3": js3, "3r": j3, "4": js4, "4r": j4} 
        try:
            mjsn = json.dumps(dictionary)
            load = json.loads(mjsn)
        except json.decoder.JSONDecodeError:
            return render_template('useless.html', row=alread)
        response = alread[1][1:]
        return render_template('done.html', json=load, response=response, original=request.form.get("essay"))
        # # for the record  - 1 = hook, 2 = description of hook 3 = how the author changed 4 = amount of discriptions
    else:
        return render_template("check.html")

@app.route('/learn', methods=["GET", "POST"])
def learn():
    return render_template('learn.html')
# normal end settings
if __name__ == '__main__':
    app.run(debug=True)