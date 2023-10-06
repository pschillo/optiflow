from flask import Flask, request, jsonify
from datetime import datetime
import util

app = Flask(__name__)


def find_row_by_code_and_date(df, flight_number, departure_date):
    # Use boolean indexing to find rows that match the given code and date
    matching_rows = df[(df['Code'] == flight_number) & (df['Date (MM/DD/YYYY)'] == departure_date)]

    if not matching_rows.empty:
        # If there's at least one matching row, return the first one (you can modify this as needed)
        return matching_rows.iloc[0]
    else:
        # If no matching rows were found, you can return None or raise an exception
        return None

@app.route('/get_arrival_time', methods=['GET'])
def get_time():
    flight_number = request.args.get('flight_number')
    departure_date = request.args.get('departure_date')

    if not flight_number:
        return jsonify({'error': 'Please provide a valid input_string parameter.'}), 400

    if not departure_date:
        return jsonify({'error': 'Please provide a valid input_string parameter.'}), 400

    # df_flight Call method that returns DF parsed from CSV.
    df_flight = util.create_flight_data()

    flight_information = find_row_by_code_and_date(df_flight, flight_number, departure_date)
    departure_time = flight_information['Departure']
    terminal = flight_information['Terminal']
    gate = flight_information['Gate']

    # Response data: Arrival Time, Time taken at security, Time taken at Checking, Walking Time

    response_data = {
        'flight_number': flight_number,
        'departure_date': departure_date,
        'departure_time': departure_time,
        'terminal': terminal,
        'gate': gate,
        # 'security_time': 10,
        # 'checkin_time': 10,
        # 'walking_time': 10,
        # 'arrival_time': 'time at which you need to be at the airport'
    }

    return jsonify(response_data)
