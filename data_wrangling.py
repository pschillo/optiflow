# %%
# imports
import pandas as pd
import random
from datetime import datetime

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

# %%
# create flight data datatrame

# estimate
Terminals = ['Terminal 1', 'Terminal 2']
GatesTerminal1 = ['A1', 'A2', 'A3', 'A4']
GatesTerminal2 = ['B1', 'B2', 'B3', 'B4']

flight_data_df = pd.DataFrame(columns=['Code', 'Date (MM/DD/YYYY)', 'Departure', 'Terminal', 'Gate', 'BoardingStarts'])
flight_data_df['Code'] = FAA_df['Carrier Code'].astype(str) + FAA_df['Flight Number'].astype(str)
flight_data_df['Departure'] = FAA_df['Scheduled departure time']
flight_data_df['Date (MM/DD/YYYY)'] = FAA_df['Date (MM/DD/YYYY)']

#for i in range(len(flight_data_df['Code'])):
    #flight_data_df['DateTime'][i] = FAA_df['Date (MM/DD/YYYY)'].astype(str) + ' ' + FAA_df['Scheduled departure time'].astype(str)
    #flight_data_df['DateTime'][i] = flight_data_df[i][0]
for i in range(len(flight_data_df['Departure'])):
    flight_data_df['BoardingStarts'][i] = datetime.strptime(flight_data_df['Departure'][i], '%H:%M') - datetime.strptime("00:30", '%H:%M')

# fill
for i in range(len(flight_data_df['Departure'])):
    flight_data_df['Terminal'][i] = random.choice(Terminals)
    
    if flight_data_df['Terminal'][i] == 'Terminal 1':
        flight_data_df['Gate'][i] = random.choice(GatesTerminal1)
    elif flight_data_df['Terminal'][i] == 'Terminal 2':
        flight_data_df['Gate'][i] = random.choice(GatesTerminal2)
    else: flight_data_df['Gate'][i] = 'unknown'

## %%
# inspect flight_data_df
flight_data_df.head()

# %%
# create waiting time dataframe

# read GRR Waiting Time (Security) data
waiting_time_df = pd.read_csv('wait_time_security.csv')

# %%
# inspect waiting_time dataframe
waiting_time_df

# 'Walking Time'
# 'Security Check Time, 'Check-In Time',

# %%
# datetime
time = "17:00"
buffer = "00:30"
converted = datetime.strptime(time, '%H:%M')

result = converted - datetime.strptime(buffer, '%H:%M')
print(result)

# %%
