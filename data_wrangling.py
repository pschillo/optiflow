# %%
# imports
import pandas as pd
import random

# %%
# load original flight data set, skipping description in first 7 lines
FAA_df = pd.read_csv('Detailed_Statistics_Departures.csv', skiprows=7)

# %%
# inspect
FAA_df.head()

# %%
# clean data

# drop N/A from relevant columns
FAA_df = FAA_df.dropna(axis=0,subset=['Carrier Code', 'Flight Number'])

# convert column 'Flight Number'
FAA_df['Flight Number'] = FAA_df['Flight Number'].astype('int')

# %%
# create flight data datatrame

# estimate
Terminals = ['Terminal 1', 'Terminal 2']
GatesTerminal1 = ['A1', 'A2', 'A3', 'A4']
GatesTerminal2 = ['B1', 'B2', 'B3', 'B4']

flight_data_df = pd.DataFrame(columns=['Code', 'Date', 'Departure', 'Terminal', 'Gate'])
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

# %%
# inspect flight_data_df
flight_data_df.head()

# %%
# create waiting time dataframe

waiting_time_df = pd.DataFrame(columns=['Time From', 'Average Waiting Time (Security)'])
timestamp_starts = ['05',
                    '06',
                    '07',
                    '09',
                    '10',
                    '11',
                    '12',
                    '13',
                    '14',
                    '15',
                    '16',
                    '17']

# add GRR data
for i in range(len(timestamp_starts)):
    waiting_time_df['Time From'][i] = timestamp_starts[i]

waiting_time_df['Average Waiting Time (Security)'][0] = 17.1
waiting_time_df['Average Waiting Time (Security)'][1] = 16.1
waiting_time_df['Average Waiting Time (Security)'][2] = 12.9
waiting_time_df['Average Waiting Time (Security)'][3] = 9.7
waiting_time_df['Average Waiting Time (Security)'][4] = 3.1
waiting_time_df['Average Waiting Time (Security)'][5] = 17.1
waiting_time_df['Average Waiting Time (Security)'][6] = 11.6
waiting_time_df['Average Waiting Time (Security)'][7] = 9.6
waiting_time_df['Average Waiting Time (Security)'][8] = 7.6
waiting_time_df['Average Waiting Time (Security)'][9] = 5.6
waiting_time_df['Average Waiting Time (Security)'][10] = 3.6
waiting_time_df['Average Waiting Time (Security)'][11] = 1.7
waiting_time_df['Average Waiting Time (Security)'][12] = 0
waiting_time_df['Average Waiting Time (Security)'][13] = 0

# %%
# inspect waiting_time dataframe
waiting_time_df

#, 'Check-In Time', 'Security Check Time', 'Boarding Time', 'Walking Time'


# %%
