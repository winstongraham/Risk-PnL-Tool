import yfinance as yf

def fetch_price_data(symbols, period="1mo"): 
    data = yf.Tickers(symbols)
    return data.history(period=period)
    """
    symbols: list of strings (e.g., ["AAPL", "TSLA"])
    Returns: pandas DataFrame of adjusted close prices
    """
def parse_input_list(str_input):
    """
    Turns comma-separated string into a cleaned list.
    """