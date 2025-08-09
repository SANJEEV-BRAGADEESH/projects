
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Automatically get the path of the CSV in the same folder as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'TCS.NSE.csv')

# Read dataset
df = pd.read_csv(csv_path)

# Convert Date column to datetime if present
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# Show basic info
print("Dataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Plot settings
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# 1. Closing Price Over Time
if 'Close' in df.columns:
    plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
    plt.title('TCS Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig(os.path.join(script_dir, 'closing_price.png'))
    plt.close()

# 2. Volume Over Time
if 'Volume' in df.columns:
    plt.plot(df['Date'], df['Volume'], label='Volume', color='orange')
    plt.title('TCS Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.savefig(os.path.join(script_dir, 'volume_over_time.png'))
    plt.close()

# 3. Daily Returns
if 'Close' in df.columns:
    df['Daily Return'] = df['Close'].pct_change(fill_method=None)
    plt.plot(df['Date'], df['Daily Return'], label='Daily Return', color='green')
    plt.title('TCS Daily Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.savefig(os.path.join(script_dir, 'daily_returns.png'))
    plt.close()

# 4. Histogram of Daily Returns
if 'Daily Return' in df.columns:
    df['Daily Return'].hist(bins=50, figsize=(10, 6))
    plt.title('Histogram of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(script_dir, 'daily_returns_hist.png'))
    plt.close()

# 5. Moving Averages
if 'Close' in df.columns:
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close', color='blue')
    plt.plot(df['Date'], df['MA50'], label='MA50', color='red')
    plt.plot(df['Date'], df['MA200'], label='MA200', color='green')
    plt.title('TCS Closing Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(os.path.join(script_dir, 'moving_averages.png'))
    plt.close()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig(os.path.join(script_dir, 'correlation_heatmap.png'))
plt.close()

print("\nAnalysis complete! Charts have been saved in the same folder as this script.")
