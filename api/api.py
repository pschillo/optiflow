from flask import Flask, request, jsonify
from datetime import time, datetime, timedelta
import pandas as pd
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


def find_row_by_departure_hour(df, departure_hour, departure_airport):
    # Use boolean indexing to find rows that match the given departure_hour
    matching_rows = df[(df['Time_From'] == departure_hour) & (df['Identifier'] == departure_airport)]

    if not matching_rows.empty:
        # If there's at least one matching row, return the first one (you can modify this as needed)
        return matching_rows.iloc[0]
    else:
        # If no matching rows were found, you can return None or raise an exception
        return None


def create_waiting_df():
    waiting_times_df = pd.read_csv('wait_time.csv')
    waiting_times_df['Security'] = waiting_times_df['Security'].astype(float)
    waiting_times_df['Check-In'] = waiting_times_df['Check-In'].astype(float)
    waiting_times_df['Walking'] = waiting_times_df['Walking'].astype(float)
    return waiting_times_df


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
    departure_airport = flight_information['Origin']

    departure_hour = int(departure_time[:2])
    waiting_times_df = create_waiting_df()
    waiting_times_for_flight = find_row_by_departure_hour(waiting_times_df, departure_hour, departure_airport)
    security_waiting_time = waiting_times_for_flight['Security']
    checkin_waiting_time = waiting_times_for_flight['Check-In']
    walking_time = waiting_times_for_flight['Walking']
    parsed_time = datetime.strptime(departure_time, "%H:%M")

    arrival_time = parsed_time - timedelta(minutes=security_waiting_time+checkin_waiting_time+walking_time)

    response_data = {
        'flight_number': flight_number,
        'departure_date': departure_date,
        'scheduled_departure_time': departure_time,
        'actual_departure_time': departure_time,
        'terminal': flight_information['Terminal'],
        'gate': flight_information['Gate'],
        'arrival_time': str(arrival_time.time()),
        'security_time': security_waiting_time,
        'checkin_time': checkin_waiting_time,
        'walking_time': walking_time,
        'departure_airport': departure_airport,
        'arrival_airport': flight_information['Destination']
    }

    return jsonify(response_data)
