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

    mean_idx = data.index[data['Time_From'] == 17][0]
    mean = float(data['Security'][mean_idx])

    security = random.gauss(mu=mean,sigma=0.5)

    return abs(security)
