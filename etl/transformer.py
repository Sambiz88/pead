import json
import utils

def clean():

def transform():

    ### TRANSFORM ###

    dirty_data = utils.load_json_data()


    ## Clean ##
    clean_data = [entry for entry in dirty_data if all(value is not None for value in entry.values())]

    with open('data.json', 'w') as f:
        json.dump(clean_data, f, indent=4)


    ## Standardize ##
    with open('data.json', 'r') as f:
        incomplete_data = json.load(f)

    for entry in incomplete_data:
        entry['epsDelta'] = (entry['epsActual'] - entry['epsEstimated'])/entry['epsEstimated']

    import yfinance as yf
    import datetime as dt
    from zoneinfo import ZoneInfo

    for entry in incomplete_data:
        stock = yf.Ticker(entry['symbol'])
        earnings_history = stock.earnings_dates
        earnings_history_sorted = earnings_history.sort_index(ascending=False)

        datetime_str = earnings_history_sorted.index[0].strftime("%Y-%m-%d %H:%M:%S")

        entry['date'] = datetime_str

        print(entry['symbol'])
    
    with open('data.json', 'w') as file:
        json.dump(incomplete_data, file, indent=4)

