from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is working!"})

@app.route('/greet', methods=['POST'])
def greet_user():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"greeting": f"Hello, {name}!"})

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide both 'num1' and 'num2'"}), 400

    try:
        total = float(num1) + float(num2)
    except ValueError:
        return jsonify({"error": "Invalid number input"}), 400

    return jsonify({"sum": total})


if __name__ == '__main__':
    app.run(debug=True)
