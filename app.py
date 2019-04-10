from flask import Flask, render_template, request, redirect, jsonify, json, url_for
from db import insert_method, select_method

app = Flask(__name__)

def order_dict(dict_data):
    import collections
    od = collections.OrderedDict(sorted(dict_data.items()))
    return od


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result.html')
def result():
    return render_template('result.html', message = request.args.get('message'))

@app.route('/handle_data', methods = ['POST', 'GET'])
def handle_data():
    if request.method == 'POST':
        # Get data from POST request
        result = request.form

        # Create empty dict to store the data
        new_dict = dict()

        # Loop through the data and extract key:value pairs
        for key, value in result.items():
            # Append kay:value pairs in the empty dict
            new_dict.update({key: value})
        
        insert_method(**new_dict)
        select_method()

        print "User input: ", result.items()
        # return redirect( url_for( 'result', message=result.items() ) )
        return render_template('result.html', view = result.items())

if __name__ == "__main__":
    app.run(debug=True)