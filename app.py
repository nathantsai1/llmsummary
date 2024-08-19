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

        # get information from json
        alread = reads(response)
        hi = alread
        jsoned = json.loads(hi)

        # and sort it
        # by reviews(numbers)
        j1 = jsoned["1"][0]
        j2 = jsoned["2"][0]
        j3 = jsoned["3"][0]
        j4 = jsoned["4"][0]

        # and strings
        js1 = jsoned["1"]
        js2 = jsoned["2"]
        js3 = jsoned["3"]
        js4 = jsoned["4"]
        for i in range(0, 3):
            # deletes number
            js1 = js1 - js1[0]
            js2 = js2 - js2[0]
            js3 = js3 - js3[0]
            js4 = js4 - js4[0]
        # make json(1 = string, 1r = rating)
        dictionary = {"1": js1, "1r": j1, "2": js2, "2r": j2, "3": js3, "3r": j3, "4": js4, "4r": j4} 
        mjsn = json.dumps(dictionary)

        return render_template('done.html', json=mjsn, response=alread[1])
        # # for the record  - 1 = hook, 2 = description of hook 3 = how the author changed 4 = amount of discriptions
    else:
        # with open('no.txt', 'r') as file:
        #     # Read the entire content of the file
        #     content = file.read()
        # alread = reads(content)
        # hi = alread[0]
        # json_object = json.loads(hi)
        # return json_object
        # # for the record  - 1 = hook, 2 = description of hook 3 = 
        # return jsonify(alread[0])
        return render_template("check.html")

# normal end settings
if __name__ == '__main__':
    app.run(debug=True)