from flask import Flask, request, jsonify
from simple_calculator.calculator import add, subtract

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.get_json()
    result = subtract(data['a'], data['b'])
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)