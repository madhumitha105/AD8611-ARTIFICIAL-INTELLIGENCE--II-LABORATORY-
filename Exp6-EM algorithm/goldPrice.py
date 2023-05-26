import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from hmmlearn import hmm 
 
base_dir = "https://github.com/natsunoyuki/Data_Science/blob/master/gold/gold/gold_price_usd.csv?raw=True" 
 
data = pd.read_csv(base_dir) 
 
# Convert the datetime from str to datetime object. 
data["datetime"] = pd.to_datetime(data["datetime"]) 
 
# Determine the daily change in gold price. 
data["gold_price_change"] = data["gold_price_usd"].diff() 
 
# Restrict the data to later than 2008 Jan 01. 
data = data[data["datetime"] >= pd.to_datetime("2008-01-01")] 
 
# Plot the daily gold prices as well as the daily change. 
plt.figure(figsize = (15, 10)) 
plt.subplot(2,1,1) 
plt.plot(data["datetime"], data["gold_price_usd"]) 
plt.xlabel("datetime") 
plt.ylabel("gold price (usd)") 
plt.grid(True) 
plt.subplot(2,1,2) 
plt.plot(data["datetime"], data["gold_price_change"]) 
plt.xlabel("datetime") 
plt.ylabel("gold price change (usd)") 
plt.grid(True) 
plt.show() 