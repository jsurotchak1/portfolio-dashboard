import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from fetch_data import fetch_stock_data

# Load current S&P 500 stocks and hold in memory from Wikipedia. Add SPY to compare to individual stocks.
@st.cache_data
def get_sp500_tickers():
    headers = {"User-Agent": "Mozilla/5.0"}
    get_tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", storage_options=headers)[0]
    tickers = get_tickers["Symbol"].tolist()
    tickers.append("SPY")
    tickers.sort()
    return tickers

@st.cache_data
def get_risk_free_rate():
    irx_data = yf.download("^IRX", period="5d")
    return irx_data["Close"].iloc[-1].values[0] / 100

# Greeting for webpage
st.title("Portfolio Performance Dashboard")
st.write("Welcome to my portfolio analyzer")

# Handles the tickers selected by user
selected_tickers = st.multiselect(
    "Select stocks for your portfolio",
    options=get_sp500_tickers(),
    default=['AAPL', 'GOOGL', 'JPM', 'MSFT', 'SPY'],
    max_selections=10
)

# Handles if no tickers are selected
if len(selected_tickers) == 0:
    st.warning("Please select at least one stock")
    st.stop()

# Fetch live data based on selected tickers
df = fetch_stock_data(selected_tickers)
close_prices = df["Close"]

# Calculate returns
daily_returns = close_prices.pct_change()
cumulative_returns = (1 + daily_returns).cumprod()

# Cumulative returns chart
st.subheader("Cumulative Returns vs S&P 500")
st.write("How much $1 invested a year ago would be worth today")
st.line_chart(cumulative_returns)

# Volatility
volatility = daily_returns.std()
annualized_volatility = volatility * np.sqrt(252)

# Sharpe ratio
risk_free_rate = get_risk_free_rate()
annual_return = cumulative_returns.iloc[-1] - 1
sharpe_ratio = (annual_return - risk_free_rate) / annualized_volatility

# Max drawdown
rolling_max = close_prices.cummax()
drawdown = (close_prices - rolling_max) / rolling_max
max_drawdown = drawdown.min()

# Summary table
summary = pd.DataFrame({
    "Annualized Volatility": annualized_volatility,
    "Sharpe Ratio": sharpe_ratio,
    "Max Drawdown": max_drawdown
})

# Display risk metrics for each selected stock
st.subheader("Risk Metrics Summary")
st.write(summary)

# Drawdown chart
st.subheader("Drawdown Chart")
st.write("How far each stock fell from its peak at any point in time")
st.line_chart(drawdown)

# Risk-return scatter plot
st.subheader("Risk-Return Scatter Plot")

fig = px.scatter(
    x=annualized_volatility,
    y=annual_return,
    text=annualized_volatility.index,
    labels={"x": "Annualized Volatility (Risk)", "y": "Annual Return"},
)

fig.update_traces(textposition="top center", marker=dict(size=12))
st.plotly_chart(fig)