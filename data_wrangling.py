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
