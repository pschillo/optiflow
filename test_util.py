# %%
# setup
import pandas as pd
import random
from util import estimate_time_security, create_flight_data, estimate_time_checkin
import datetime

# %%
# test estimate_time_security
data = pd.read_csv('wait_time.csv')
time = "05:00"

test = estimate_time_checkin(time, data, "GRR")
print(test)

# %%
# test estimate_time_security
data = pd.read_csv('wait_time.csv')
time = "17:00"

test = estimate_time_security(time, data, "GRR")
print(test)

# %%
# test create_flight_data
test_df = create_flight_data()

test_df


# %%
