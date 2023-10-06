# %%
# setup
import pandas as pd
import random

# estimate security
def estimate_time_security(time, time_df):

    time = time
    data = time_df

    # convert time format
    time = str(time)
    hours = time[:2]

    mean = data.iloc[data['Time_From'] == hours]
    

    security = mean

    return security

# %%
# test
data = pd.read_csv('wait_time_security.csv')
time = "17:00"

test = estimate_time_security(time, data)
print(test)

# %%
# inspect
data

# %%
# test
data.index[data['BoolCol'] == True]
