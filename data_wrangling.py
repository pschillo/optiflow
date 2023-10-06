# %%
# imports
import pandas as pd

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
# create final datatrame

Terminals = ['Terminal 1']
Gates = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4']

data_df = pd.DataFrame(columns=['Code', 'Departure', 'Terminal', 'Gate'])
data_df['Code'] = FAA_df['Carrier Code'].astype(str) + FAA_df['Flight Number'].astype(str)
data_df['Departure'] = FAA_df['Scheduled departure time']
data_df['Terminal'] = 'Terminal 1'
data_df['Gate'] = x

# %%
# inspect data_df
data_df.head()

# %%
