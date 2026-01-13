import json
import storage

def clean():
    
    dirty_data = storage.read_json()

    # Remove stocks with missing earnings dates (usually foreign or delisted stocks)
    clean_data = [entry for entry in dirty_data if all(value is not None for value in entry.values())]

    storage.write_json(clean_data)
    

def standardize():
        
    import yfinance as yf
    import datetime as dt
    from zoneinfo import ZoneInfo
    today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = storage.read_json()

    i = 5
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
        i = i-1
        if i<0:
            break


    storage.write_json(data)


def enrich():

    data = storage.read_json()

    for entry in data:
        entry['epsDelta'] = (entry['epsActual'] - entry['epsEstimated'])/entry['epsEstimated']

    storage.write_json(data)




def transform():
    clean()
    standardize()
    enrich()
