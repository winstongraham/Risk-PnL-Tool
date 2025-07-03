
import streamlit as st
from portfolio import calculate_pnl
from risk_metrics import calculate_sharpe, calculate_drawdown, calculate_var
from utils import fetch_price_data
import datetime
 
st.title("🏦 Bank Risk & PnL Dashboard")
 
st.sidebar.header("Desk Position Setup")
 
symbols = st.sidebar.text_input("Instruments (comma separated)", "AAPL, TSLA").upper().split(",")
quantities = st.sidebar.text_input("Position Sizes (comma separated)", "1000, 500").split(",")
entry_prices = st.sidebar.text_input("Entry Prices (comma separated)", "150, 700").split(",")
 #TODO insert multiple periods
#start_date = st.sidebar.date_input("Start Date", datetime.date(2023, 1, 1))
 
# Format as internal desk positions
positions = [
    {"symbol": sym.strip(), "quantity": float(q), "entry_price": float(p)}
    for sym, q, p in zip(symbols, quantities, entry_prices)
]
# Get price history
prices = fetch_price_data([p["symbol"] for p in positions], period="1mo")
# pnl_df = calculate_pnl(positions, prices)

st.dataframe(data=prices)
'''
 
 
st.subheader("📈 Mark-to-Market (MTM) Portfolio Value")
st.line_chart(pnl_df["portfolio_value"])
 
st.subheader("📋 PnL Overview (Unrealized)")
st.dataframe(pnl_df.tail())
 
st.subheader("📊 Risk Summary (Daily Returns-Based)")
sharpe = calculate_sharpe(pnl_df["daily_returns"])
drawdown = calculate_drawdown(pnl_df["portfolio_value"])
var = calculate_var(pnl_df["daily_returns"])
 
st.metric("Sharpe Ratio", f"{sharpe:.2f}")
st.metric("Max Drawdown", f"{drawdown:.2%}")
st.metric("VaR (95%)", f"${var:.2f}")
'''