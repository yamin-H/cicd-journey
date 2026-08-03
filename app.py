from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


@app.route('/')
def home():
    return jsonify({
        'status': 'running',
        'message': 'CI/CD Journey App'
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '3.0'
    })


@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    result = add(a, b)
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': result})


@app.route('/subtract/<int:a>/<int:b>')
def subtract_route(a, b):
    result = subtract(a, b)
    return jsonify({'operation': 'subtract', 'a': a, 'b': b, 'result': result})


@app.route('/multiply/<int:a>/<int:b>')
def multiply_route(a, b):
    result = multiply(a, b)
    return jsonify({'operation': 'multiply', 'a': a, 'b': b, 'result': result})


@app.route('/divide/<int:a>/<int:b>')
def divide_route(a, b):
    result = divide(a, b)
    if result is None:
        return jsonify({'error': 'division by zero'}), 400
    return jsonify({'operation': 'divide', 'a': a, 'b': b, 'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)