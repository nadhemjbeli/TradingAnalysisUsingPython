# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# Store the data
FB=pd.read_csv("FB21.csv")
# Show the first 5 elements of the data
FB.head()
# Set the date as the Index for the data
FB = FB.set_index(pd.DatetimeIndex(FB["date"].values))
# Show the data
FB
# Visually show the price
plt.figure(figsize=(12.2, 4.5))
plt.plot(FB.index,FB["Adj Close Price"], label = "Adj Close Price")
plt.title("Adj.Close Price History")
plt.xlabel("2020 to 2021 ", fontsize = 18)
plt.ylabel("Adj. Close Price USD ($)",fontsize=18)
plt.show()
# Prepare the data to Calculate the RSI

# Get the difference in price
delta = FB['Adj Close Price'].diff(1)
delta
# Get rid of NaN
delta = delta.dropna()
delta

# Get the positive gains (up) and the negative gains (down)
up = delta.copy()
down= delta.copy()
up[up<0] = 0
down[down>0] = 0

# Get the time period
period = 14
# Calculate the average gain and the average loss
AVG_Gain = up.rolling(window=period).mean()
AVG_Loss = abs(down.rolling(window=period).mean())

# Calculate the RSI

# Calculate the Relative Strength (RS)
RS = AVG_Gain / AVG_Loss
# Calculate the Relative Strength Index (RSI)
RSI = 100.0 - (100.0 / (1.0 + RS))

#Show the RSI Visually
plt.figure(figsize=(12.2,4.5))
RSI.plot()
plt.show()

# Put it all together

# Create a new data frame
new_df = pd.DataFrame()
new_df['Adj Close Price'] = FB['Adj Close Price']
new_df['RSI']=RSI
new_df

# Visually show the adjusted close price and RSI

# Plot the adjusted close price
plt.figure(figsize=(12.2,4.5))
plt.plot(new_df.index, new_df['Adj Close Price'])
plt.title('Adj. Close Price History')
plt.legend(new_df.columns.values, loc = 'upper left')
plt.show()
# Plot the corresponding RSI values and significant levels
plt.figure(figsize=(12.2,4.5))
plt.title('RSI Plot')
plt.plot(new_df.index, new_df['RSI'])
plt.axhline(0,linestyle='--', alpha = 0.5, color='gray')
plt.axhline(10,linestyle='--', alpha = 0.5, color='orange')
plt.axhline(20,linestyle='--', alpha = 0.5, color='green')
plt.axhline(40,linestyle='--', alpha = 0.5, color='red')
plt.axhline(60,linestyle='--', alpha = 0.5, color='red')
plt.axhline(80,linestyle='--', alpha = 0.5, color='green')
plt.axhline(90,linestyle='--', alpha = 0.5, color='orange')
plt.axhline(100,linestyle='--', alpha = 0.5, color='gray')
plt.show()