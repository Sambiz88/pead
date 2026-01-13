from datetime import datetime, timedelta
import zoneinfo
import yfinance as yf

def is_call_in_am(date_str: str) -> bool:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.hour < 12

def get_close_price(symbol: str, date_str: str) -> float:

    # Convert string to datetime
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    
    # yfinance end date is exclusive, so add 1 day
    next_day = date + timedelta(days=1)
    
    # Fetch historical data
    ticker = yf.Ticker(symbol)
    hist = ticker.history(
        start=date.strftime("%Y-%m-%d"),
        end=next_day.strftime("%Y-%m-%d")
    )
    
    if hist.empty:
        return None  # Market closed, or ticker invalid
    else:
        # Return the close price
        print(hist["Close"].iloc[0])

        return hist["Close"].iloc[0]

