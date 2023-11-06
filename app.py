from flask import Flask, request, jsonify
from simple_calculator.calculator import add, subtract

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_route():
    """
     Add a route to the database. This is a POST request to / api / v1 / routes?a = b
     
     :returns: JSON with result of add operation as well as error message if something went wrong ( for example if there is a conflict
    """
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract_route():
    """
     Subtract two numbers and return the result. This is a route for subtraction of two numbers. The parameters a and b are the numbers to be subtracted and the result is a JSON object with the result of the operation.
     
     :returns: JSON object with the result of the operation as a JSON object with the result of the operation as a
    """
    data = request.get_json()
    result = subtract(data['a'], data['b'])
    return jsonify(result=result)

# Run the app if the __main__ is the main app. run debug True
if __name__ == '__main__':
    app.run(debug=True)