# pip3 install bs4 requests yfinance
import requests
from bs4 import BeautifulSoup
import csv
import yfinance as yf

# Function to retrieve stock data and create CSV file
def get_stock_data_and_create_csv(symbols, csv_file_path):
    stock_data = []

    # Define the date range for the last month
    start_date = (yf.Ticker(symbols[0])).history(period='1mo').index[0]
    end_date = (yf.Ticker(symbols[0])).history(period='1mo').index[-1]
    print(start_date)

    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            history = stock.history(start=start_date, end=end_date)

            # Check if there is any data available
            if not history.empty:
                for index, row in history.iterrows():
                    stock_data.append({
                        "Symbol": symbol,
                        "Date": index.strftime("%d-%m-%Y"),
                        "Close Price": row["Close"],
                        "Volume": row["Volume"]
                    })
            else:
                print(f"No data found for {symbol}")

        except yf.TickerError as e:
            print(f"Error retrieving data for {symbol}: {e}")
        except yf.YFinanceError as e:
            print(f"Error for {symbol}: {e}")

    # Save stock data to CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Symbol', 'Date', 'Close Price', 'Volume']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write stock data
        for data in stock_data:
            writer.writerow(data)
    
    print(f"Stock data saved to {csv_file_path}")

# Symbols you are interested in
symbols_of_interest = ['BTC-USD', 'TSLA', 'GM']

# Create CSV file with daily closing prices for the last month
csv_file_path = "stock_data_gapminder.csv"
get_stock_data_and_create_csv(symbols_of_interest, csv_file_path)