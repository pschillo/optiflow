# %%
# setup
import pandas as pd
import random
from util import *

# %%
# test
data = pd.read_csv('wait_time_security.csv')
time = "17:00"

test = estimate_time_security(time, data)
print(test)

# %%
