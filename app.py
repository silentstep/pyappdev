from flask import Flask, render_template, request, redirect, jsonify, json, url_for, session
import db

app = Flask(__name__)
app.secret_key = ".."
db_conn = db.Worker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    user_input = request.form
    user_input_dict = dict()

    for key, value in user_input.items():
        user_input_dict.update({key: value})

    if user_input_dict['server']:
        # session['message'] = user_input_dict
        # print session
        # session.clear()
        db_conn.qry_insert(**user_input_dict)
        qry_result_json = jsonify(db_conn.qry_select()[0])
        db_conn.conn.close()
        return qry_result_json

    return jsonify({'error' : 'Missing data'})


if __name__ == "__main__":
    app.run(debug=True)