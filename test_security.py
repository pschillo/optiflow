# %%
# setup
import pandas as pd
import random
from util import estimate_time_security

# %%
# test
data = pd.read_csv('wait_time.csv')
time = "17:00"

test = estimate_time_security(time, data)
print(test)

# %%
