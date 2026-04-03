# Portfolio Performance Dashboard

A web-based portfolio analysis tool that compares stocks against the S&P 500 using real-time data and key risk metrics.

## Live Demo
[Click here to view the live app](https://portfolio-dashboard-surotj.streamlit.app/)

## Features
- Select any stocks from the S&P 500 to analyze
- Cumulative returns chart — how much $1 invested a year ago would be worth today
- Risk metrics table — annualized volatility, Sharpe ratio, and max drawdown
- Drawdown chart — shows the worst dips from peak over time
- Risk-return scatter plot — visualizes risk vs reward for each stock

## Tech Stack
- Python
- pandas — data manipulation
- numpy — financial calculations
- yfinance — live stock data from Yahoo Finance
- Streamlit — interactive web app
- SQLite — database layer for storing historical prices
- Plotly — interactive charts

## How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run dashboard.py`

## What I Learned
Built this project to develop skills in financial data analysis and Python development. 
Key concepts learned include data manipulation with pandas, SQL database design, 
financial metric calculations, and deploying interactive web applications.