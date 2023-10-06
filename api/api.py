from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/get_time', methods=['GET'])
def get_time():
    input_string = request.args.get('input_string')

    if not input_string:
        return jsonify({'error': 'Please provide a valid input_string parameter.'}), 400

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response_data = {
        'input_string': input_string,
        'current_time': current_time
    }

    return jsonify(response_data)
