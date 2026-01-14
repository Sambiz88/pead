import json
import storage
from utils import is_call_in_am, get_close_price
import yfinance as yf
from datetime import datetime, timedelta

def clean():
    
    dirty_data = storage.read_json()

    # Remove stocks with missing earnings dates (usually foreign or delisted stocks)
    clean_data = [entry for entry in dirty_data if all(value is not None for value in entry.values())]

    storage.write_json(clean_data)
    

def standardize():
        
    
    import datetime as dt
    from zoneinfo import ZoneInfo
    today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = storage.read_json()

 
    for entry in data:

        print(entry['symbol'])
        stock = yf.Ticker(entry['symbol'])
        earnings_history = stock.earnings_dates
        earnings_history_sorted = earnings_history.sort_index(ascending=False)

        datetime_str = earnings_history_sorted.index[0].strftime("%Y-%m-%d %H:%M:%S")

        if datetime_str >= today:
            datetime_str = earnings_history_sorted.index[1].strftime("%Y-%m-%d %H:%M:%S")
                
        entry['date'] = datetime_str
                 
        print(datetime_str)

    storage.write_json(data)


def enrich():

    data = storage.read_json()

    for entry in data:
        entry['surprise'] = (entry['epsActual'] - entry['epsEstimated'])/abs(entry['epsEstimated'])


    storage.write_json(data)


def pre_earnings_price():
    data = storage.read_json()

    for object in data:
        if is_call_in_am(object["date"]) == False:
            object["preEarningsPrice"] = get_close_price(object["symbol"], object["date"])
        
        else:
            date = datetime.strptime(object["date"], "%Y-%m-%d %H:%M:%S")
            date = date-timedelta(days=1)
            date = date.strftime("%Y-%m-%d %H:%M:%S")

            object["preEarningsPrice"] = get_close_price(object["symbol"], date)

    storage.write_json(data)

def transform():
    clean()
    standardize()
    enrich()
