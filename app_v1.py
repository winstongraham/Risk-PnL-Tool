import streamlit as st
import yfinance as yf # Ensure yfinance is installed
import pandas as pd
import numpy as np 
from datetime import datetime

st.set_page_config(page_title="Risk & PnL Tool", layout="wide")
st.title("📊 Portfolio Tracker with Risk Metrics")

# --- Sidebar Inputs ---
st.sidebar.header("📥 Portfolio Input")
num_stocks = st.sidebar.number_input("How many stocks in your portfolio?", min_value=1, max_value=10, value=2)

portfolio = []
for i in range(num_stocks):
    st.sidebar.subheader(f"Stock {i+1}")
    ticker = st.sidebar.text_input(f"Ticker {i+1}", value="AAPL", key=f"ticker_{i}")
    quantity = st.sidebar.number_input(f"Quantity {i+1}", min_value=1, value=10, key=f"qty_{i}")
    buy_price = st.sidebar.number_input(f"Buy Price {i+1}", min_value=0.0, value=100.0, key=f"bp_{i}")
    portfolio.append({"ticker": ticker.upper(), "quantity": quantity, "buy_price": buy_price})

# --- Data Fetching & Processing ---
results = []
for stock in portfolio:
    ticker = stock["ticker"]
    try:
        data = yf.Ticker(ticker).history(period="1d")
        current_price = data["Close"].iloc[-1]
        unrealised_pnl = (current_price - stock["buy_price"]) * stock["quantity"]
        mtm_value = current_price * stock["quantity"]
        results.append({
            "Ticker": ticker,
            "Qty": stock["quantity"],
            "Buy Price": stock["buy_price"],
            "Current Price": round(current_price, 2),
            "MTM Value": round(mtm_value, 2),
            "Unrealized PnL": round(unrealised_pnl, 2)
        })
    except Exception as e:
        st.warning(f"Couldn't fetch data for {ticker}: {e}")

# --- Display ---
if results:
    df = pd.DataFrame(results)
    total_value = df["MTM Value"].sum()
    total_pnl = df["Unrealized PnL"].sum()
    st.subheader("📈 Portfolio Summary")
    st.dataframe(df.set_index("Ticker"))

    st.markdown(f"""
        **Total MTM Value:** ${total_value:,.2f}  
        **Total Unrealized PnL:** ${total_pnl:,.2f}
    """)
else:
    st.info("Enter valid tickers to see portfolio summary.")