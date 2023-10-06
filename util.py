# %%
# setup
import pandas as pd
import random

def create_flight_data():

    # %%
    # load original flight data set, skipping description in first 7 lines
    FAA_df = pd.read_csv('Detailed_Statistics_Departures.csv', skiprows=7)

    ## %%
    # inspect
    FAA_df.head()

    ## %%
    # clean data

    # drop N/A from relevant columns
    FAA_df = FAA_df.dropna(axis=0,subset=['Carrier Code', 'Flight Number'])

    # convert column 'Flight Number'
    FAA_df['Flight Number'] = FAA_df['Flight Number'].astype('int')

    ## %%
    # create flight data datatrame

    # estimate
    Terminals = ['Terminal 1', 'Terminal 2']
    GatesTerminal1 = ['A1', 'A2', 'A3', 'A4']
    GatesTerminal2 = ['B1', 'B2', 'B3', 'B4']

    flight_data_df = pd.DataFrame(columns=['Code', 'Departure', 'Terminal', 'Gate'])
    flight_data_df['Code'] = FAA_df['Carrier Code'].astype(str) + FAA_df['Flight Number'].astype(str)
    flight_data_df['Departure'] = FAA_df['Scheduled departure time']
    flight_data_df['Date (MM/DD/YYYY)'] = FAA_df['Date (MM/DD/YYYY)']

    # fill
    for i in range(len(flight_data_df['Departure'])):
        flight_data_df['Terminal'][i] = random.choice(Terminals)
        
        if flight_data_df['Terminal'][i] == 'Terminal 1':
            flight_data_df['Gate'][i] = random.choice(GatesTerminal1)
        elif flight_data_df['Terminal'][i] == 'Terminal 2':
            flight_data_df['Gate'][i] = random.choice(GatesTerminal2)
        else: flight_data_df['Gate'][i] = 'unknown'

    return flight_data_df

# estimate security
def estimate_time_security(time, time_df):

    time = time
    data = time_df

    # convert time format
    time = str(time)
    hours = time[:2]

    mean_idx = data.index[data['Time_From'] == float(hours)][0]
    mean = float(data['Security'][mean_idx])

    security = random.gauss(mu=mean,sigma=0.5)

    return abs(security)

# %%
