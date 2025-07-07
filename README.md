📘 Risk & PnL Tool Documentation

This document outlines the structure and functionality of the Risk and PnL Dashboard project modules: portfolio.py, risk_metrics.py, and utils.py, along with how they integrate into the Streamlit app.

📦 Project Overview

The Risk and Profit & Loss (PnL) Tool is a financial dashboard built in Python using Streamlit. It is designed from the perspective of a bank to manage its trading desk’s exposure. It calculates position-level PnL, portfolio-level metrics, and evaluates key risk metrics like Sharpe ratio, drawdowns, and Value at Risk (VaR).

🧮 portfolio.py

This module handles all computations related to profit and loss, returns, and portfolio valuation.

🔧 Functions

calculate_pnl(prices, entry_prices, quantities)

Description: Computes the unrealized PnL for each instrument.

Inputs:

prices: dict of latest market prices ({"AAPL": 160.0})

entry_prices: dict of entry prices ({"AAPL": 150.0})

quantities: dict of quantities ({"AAPL": 1000})

Returns: dict of unrealized PnL per instrument

calculate_portfolio_value(prices, quantities)

Description: Computes the total value of the portfolio using current market prices.

Returns: Total portfolio value

calculate_daily_returns(price_series)

Description: Computes daily returns from historical price data.

Inputs: pandas DataFrame with symbols as columns

Returns: DataFrame of daily % returns

📊 risk_metrics.py

This module contains functions that calculate financial risk metrics for the portfolio.

🔧 Functions

calculate_sharpe(returns, risk_free_rate=0.01)

Description: Computes Sharpe ratio.

Inputs:

returns: Series or DataFrame of returns

risk_free_rate: Annual risk-free rate (default 1%)

Returns: Sharpe ratio (float)

calculate_drawdown(equity_curve)

Description: Calculates drawdowns over time and identifies the max drawdown.

Inputs: pandas Series of portfolio value

Returns: drawdown Series and max drawdown value

calculate_var(returns, confidence_level=0.95)

Description: Calculates Value at Risk (VaR) using historical simulation or percentile method.

Inputs:

returns: Series of returns

confidence_level: e.g., 0.95

Returns: float VaR value

🔧 utils.py

This is the helper module that includes utility functions used throughout the app.

🔧 Functions

fetch_price_data(symbols, start, end)

Description: Pulls historical adjusted close prices from Yahoo Finance using yfinance.

Returns: pandas DataFrame of prices

parse_input_list(str_input)

Description: Parses a comma-separated string from the UI into a clean list.

🖥️ Streamlit App Snippet

st.title("\U0001F3E6 Bank Risk & PnL Dashboard")

symbols = st.sidebar.text_input("Instruments (comma separated)", "AAPL, TSLA").upper().split(",")
quantities = st.sidebar.text_input("Position Sizes (comma separated)", "1000, 500").split(",")
entry_prices = st.sidebar.text_input("Entry Prices (comma separated)", "150, 700").split(",")

This UI feeds inputs into the tool and passes them to your helper and PnL functions.

✅ Summary

File

Responsibilities

portfolio.py

PnL, returns, and valuation logic

risk_metrics.py

Sharpe ratio, drawdown, VaR calculations

utils.py

Data fetching, input parsing

Each module is self-contained and easy to test independently. The Streamlit app then brings them together into an interactive dashboard experience.

For further extension, consider adding:

Trade logs

Historical PnL visualization

Risk limits breach alerts

