# pip3 install matplotlib datetime
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to analyze stock price trend and provide recommendation
def analyze_stock_trend(stock_symbol, csv_file_path):
    # Read stock data from CSV
    stock_data = pd.read_csv(csv_file_path, parse_dates=['Date'], dayfirst=True)  # Specify dayfirst if needed

    # Filter data for the last 30 days
    last_30_days = stock_data[stock_data['Date'] >= stock_data['Date'].max() - pd.DateOffset(days=30)]

    # Plot the stock prices
    plt.figure(figsize=(10, 6))
    plt.plot(last_30_days['Date'], last_30_days['Close Price'], label='Close Price')
    plt.title(f'Stock Price Trend for {stock_symbol} (Last 30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

    # Calculate the trend direction
    price_changes = last_30_days['Close Price'].diff()
    trend_direction = 'upward' if price_changes.mean() > 0 else 'downward' if price_changes.mean() < 0 else 'inconsistent'

    # Provide recommendation
    print(f"\nRecommendation for {stock_symbol}:")
    if trend_direction == 'upward':
        print("BUY STOCK!")
    elif trend_direction == 'downward':
        print("DO NOT BUY STOCK!")
    else:
        print("WAIT BEFORE BUYING STOCK!")

# CSV file path generated from the previous code
csv_file_path = "stock_data_gapminder.csv"

# Stock symbols of interest
symbols_of_interest = ['BTC-USD', 'TSLA', 'GM'] #'BTC-USD', 'TSLA', 'GM'

# Analyze the stock trend and provide recommendation for each stock
for symbol in symbols_of_interest:
    analyze_stock_trend(symbol, csv_file_path)