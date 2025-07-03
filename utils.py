import yfinance as yf

def fetch_price_data(symbols, period="1mo"): 
    data = yf.Tickers(symbols)
    return data.history(period=period)
    