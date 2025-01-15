import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# graph the number of views for each channel
# see if there is a correlation between the no of views and how much the price changes
# pretty graph for investors
# each influencer and their average max price increase
# if there are
# influencers vs time
# max price increase vs time

# Load the data
df = pd.read_csv("mongodb_data.csv")

# Ensure data types are correct; 'Max_Price_Ratio_Increase' should be numeric
df['Max_Price_Ratio_Increase'] = pd.to_numeric(df['Max_Price_Ratio_Increase'], errors='coerce')

# Drop any rows that have NaN values in 'Channel' or 'Max_Price_Ratio_Increase' after conversion
df = df.dropna(subset=['Channel', 'Max_Price_Ratio_Increase'])

# Calculate the mean 'Max_Price_Ratio_Increase' for each channel
channel_means = df.groupby('Channel')['Max_Price_Ratio_Increase'].mean().reset_index()

# Sort the channels based on the mean 'Max_Price_Ratio_Increase' in descending order
channel_means_sorted = channel_means.sort_values(by='Max_Price_Ratio_Increase', ascending=False)

# Plotting the mean 'Max_Price_Ratio_Increase' for each channel
plt.figure(figsize=(10, 6))

# Plot a subset of the channels, like the top 20 channels
top_channels = channel_means_sorted.head(20)
plt.bar(top_channels['Channel'], top_channels['Max_Price_Ratio_Increase'], alpha=0.5)

# Here we make the scatter points black by specifying color='k' (short for black)
plt.scatter(df['Channel'], df['Max_Price_Ratio_Increase'], alpha=0.5, color='k')

plt.title('Mean Max Price Ratio Increase by Channel')
plt.xlabel('Channel')
plt.ylabel('Mean Max Price Ratio Increase')
plt.xticks(rotation=90)  # Rotate Channel names for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

# Save the plot to a PNG file with a DPI of 600
plt.savefig("channel_max_price_ratio_increase.png", dpi=600)

plt.show()

print(df.columns)


# Set seaborn style
sns.set(style="whitegrid")
# Convert 'Published Date' column to datetime format
df['Published Date'] = pd.to_datetime(df['Published Date'])

# Check the data types of the 'Max Price in 7 Days' and 'Min Price in 7 Days' columns
print(df[['Max Price in 7 Days', 'Min Price in 7 Days']].dtypes)

# Convert the columns to numeric format, coercing errors to NaN
df['Max Price in 7 Days'] = pd.to_numeric(df['Max Price in 7 Days'], errors='coerce')
df['Min Price in 7 Days'] = pd.to_numeric(df['Min Price in 7 Days'], errors='coerce')

# Drop rows with NaN values in the 'Max Price in 7 Days' and 'Min Price in 7 Days' columns
df = df.dropna(subset=['Max Price in 7 Days', 'Min Price in 7 Days'])

# Plot the max and min price in 7 days as a function of cryptocurrencies
plt.figure(figsize=(12, 8))
crypto_prices = df.groupby('cryptocurrency')[['Max Price in 7 Days', 'Min Price in 7 Days']].mean().reset_index()
plt.plot(crypto_prices['cryptocurrency'], crypto_prices['Max Price in 7 Days'], label='Max Price', marker='o')
plt.plot(crypto_prices['cryptocurrency'], crypto_prices['Min Price in 7 Days'], label='Min Price', marker='o')
plt.title('Max and Min Price in 7 Days by Cryptocurrency')
plt.xlabel('Cryptocurrency')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot the number of views of each channel
plt.figure(figsize=(12, 8))
channel_views = df.groupby('Channel')['Views'].sum().reset_index()
plt.bar(channel_views['Channel'], channel_views['Views'])
plt.title('Number of Views by Channel')
plt.xlabel('Channel')
plt.ylabel('Number of Views')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Ensure data types are correct; 'Max_Price_Ratio_Increase' should be numeric
df['Max_Price_Ratio_Increase'] = pd.to_numeric(df['Max_Price_Ratio_Increase'], errors='coerce')

# Drop any rows that have NaN values in 'Channel' or 'Max_Price_Ratio_Increase' after conversion
df = df.dropna(subset=['Views', 'Max_Price_Ratio_Increase'])

# Plotting the correlation between the number of views and price change
plt.figure(figsize=(10, 6))
plt.scatter(df['Views'], df['Max_Price_Ratio_Increase'], alpha=0.5)
plt.title('Correlation between Number of Views and Max Price Increase')
plt.xlabel('Number of Views')
plt.ylabel('Max Price Increase Ratio')
plt.grid(True)
plt.tight_layout()
plt.show()

# Ensure data types are correct; 'Max_Price_Ratio_Increase' should be numeric
df['Max_Price_Ratio_Increase'] = pd.to_numeric(df['Max_Price_Ratio_Increase'], errors='coerce')

# Drop any rows that have NaN values in 'Channel' or 'Max_Price_Ratio_Increase' after conversion
df = df.dropna(subset=['Channel', 'Max_Price_Ratio_Increase'])

# Calculate the mean 'Max_Price_Ratio_Increase' for each influencer
influencer_means = df.groupby('Channel')['Max_Price_Ratio_Increase'].mean().reset_index()

# Sort the influencers based on the mean 'Max_Price_Ratio_Increase' in descending order
influencer_means_sorted = influencer_means.sort_values(by='Max_Price_Ratio_Increase', ascending=False)

# Plotting the average max price ratio increase for each influencer
plt.figure(figsize=(12, 8))
plt.bar(influencer_means_sorted['Channel'], influencer_means_sorted['Max_Price_Ratio_Increase'], color='skyblue')
plt.title('Average Max Price Ratio Increase by Influencer')
plt.xlabel('Influencer')
plt.ylabel('Average Max Price Ratio Increase')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
