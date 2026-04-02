import yfinance as yf
import streamlit as st

# Function to download data for each stock and store data in memory
@st.cache_data
def fetch_stock_data(stock_list):
    data = yf.download(stock_list, period="1y")
    return data