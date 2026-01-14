from datetime import datetime, timedelta
import zoneinfo
import yfinance as yf

def is_call_in_am(date_str) -> bool:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.hour < 12

def get_close_price(symbol: str, date: str) -> float:

    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    
    # yfinance end date is exclusive
    next_day = date + timedelta(days=3)
    
    ticker = yf.Ticker(symbol)
    hist = ticker.history(
        start=date,
        end=next_day
    )
    
    if hist.empty:
        return None  # Market closed, or ticker invalid
    else:
        print(hist["Close"].iloc[0])

        return hist["Close"].iloc[0]

