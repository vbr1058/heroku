import flask
import requests
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books =requests.get("https://assignment-machstatz.herokuapp.com/excel").text
books= json.loads(books)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Please provide a date in the url as shown</h1>
<p>/api/today?date=type yoour date<br>A prototype API for Data reading </p>'''

@app.route('/api/today/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/today', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'date' in request.args:
        date = str(request.args['date'])
        date=date.split("-")
        date=date[::-1]
        date="-".join(date)

    else:
        return "Error: No Date field provided. Please specify an date."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if date in str(book['DateTime']):
            results.append(book)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
    # except:
        # return "<center><h1>Date is not present<h1><h3>Please enter the valid date<h3><center>"
