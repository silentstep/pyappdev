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
        # Do db import here 
        return jsonify(new_dict)

    return jsonify({'error' : 'Missing data'})


if __name__ == "__main__":
    app.run(debug=True)

#@app.route('/')
#def index():
#    if 'message' in session:
#        message = session['message']
#        return render_template('index.html', message=message)
#    else:
#        return render_template('index.html')

#@app.route('/result.html')
#def result():
#    message = request.args['message']
#    return render_template('result.html', message=message)

#@app.route('/handle_data', methods = ['POST', 'GET'])
#def handle_data():
#    if request.method == 'POST':
#        # Get data from POST request
#        result = request.form
#
#        # Create empty dict to store the data
#        new_dict = dict()
#
#        # Loop through the data and extract key:value pairs
#        for key, value in result.items():
#            # Append kay:value pairs in the empty dict
#            new_dict.update({key: value})
#        
#        insert_method(**new_dict)
#        # select_method()
#
#        ## message = json.dumps(new_dict)
#        message = new_dict
#        session['message'] = message
#        print session['message']
#        # return redirect(url_for('index', message=message))
#        # return render_template('result.html', view = result.items())