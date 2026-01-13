import pandas as pd
import yfinance as yf
import datetime as dt
from zoneinfo import ZoneInfo

df = pd.read_csv('constituents.csv')

last_earnings_list = []


stock = yf.Ticker("AAPL")
earnings_history = stock.earnings_dates
earnings_history_sorted = earnings_history.sort_index(ascending=False)
datetime_str = earnings_history_sorted.index[0].strftime("%Y-%m-%d %H:%M:%S")

print(datetime_str)
print(type(datetime_str))


"""
print(dt.datetime.now())
print(type(dt.datetime.now()))
print(yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1])
print(type(yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1]))

cleand = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(cleand)
print(type(cleand))

clean = yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1].strftime("%Y-%m-%d %H:%M:%S")
print(clean)
print(type(clean))"""
"""
dt_obj = (yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1]).to_pydatetime()
dt_eastern = dt_obj.astimezone(ZoneInfo("America/New_York"))
print(dt_eastern)
"""
"""
for t in df['Symbol']:
    stock = yf.Ticker(t)
    earnings_history = stock.earnings_dates
    earnings_history_sorted = earnings_history.sort_index(ascending=False)
    
    if dt.datetime.now() >= earnings_history_sorted.index[0]:
        last_date = earnings_history_sorted.index[0]
        
    
    else:
        last_date = earnings_history_sorted.index[1]
        
    print(f"o {t}")
    last_earnings_list.append(last_date)

df['Last Earnings Call'] = last_earnings_list

"""