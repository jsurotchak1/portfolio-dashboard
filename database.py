import sqlite3
from fetch_data import fetch_stock_data

# Connect to database
conn = sqlite3.connect("portfolio.db")
print("Database connected successfully")

# Create cursor to execute SQL commands
cursor = conn.cursor()

# Create table to store stock prices
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        date TEXT,
        ticker TEXT,
        close_price REAL
    )
""")

# Default stocks for database storage - dashboard fetches live data for any ticker
stocks = ["AAPL", "MSFT", "JPM", "GOOGL", "SPY"]
df = fetch_stock_data(stocks)
close_prices = df["Close"]

# Clear existing data and insert fresh data
cursor.execute("DELETE FROM stock_prices")

for date, row in close_prices.iterrows():
    for ticker in close_prices.columns:
        price = row[ticker]
        cursor.execute("INSERT INTO stock_prices (date, ticker, close_price) VALUES (?, ?, ?)", (str(date), ticker, price))

conn.commit()
print("Data inserted successfully")