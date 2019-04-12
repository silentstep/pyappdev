from flask import Flask, render_template, request, redirect, jsonify, json, url_for, session
from db import insert_method, select_method

app = Flask(__name__)
app.secret_key = ".."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    result = request.form
    new_dict = dict()
    for key, value in result.items():
        new_dict.update({key: value})

    if new_dict['server']:
        session['message'] = new_dict
        print session
        # session.clear()
        return jsonify(new_dict)

    return jsonify({'error' : 'Missing data'})


if __name__ == "__main__":
    app.run(debug=True)