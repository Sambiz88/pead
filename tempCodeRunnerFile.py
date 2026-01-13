
print(dt.datetime.now())
print(type(dt.datetime.now()))
print(yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1])
print(type(yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1]))

cleand = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(cleand)
print(type(cleand))

clean = yf.Ticker("AAPL").earnings_dates.sort_index(ascending=False).index[1].strftime("%Y-%m-%d %H:%M:%S")
print(clean)
print(type(clean))