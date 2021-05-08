import yfinance as yf
import pprint
import pandas_datareader.data as wb
from datetime import datetime

start = datetime(2016, 9, 1)
end = datetime(2019, 9, 1)

#matches = wb.DataReader('F', 'iex', start, end)

pp = pprint.PrettyPrinter(indent=4)

tickers = ['MSFT', 'VACI', 'VCVC', 'ZNTE']


for tick in tickers:
    tick_stuff = yf.Ticker(tick)
    print(tick_stuff.history())
    print(tick)
#msft = yf.Ticker("MSFT")
#victory = yf.Ticker("VACI")
#x_10 = yf.Ticker("VCVC")

#pp.pprint(x_10._download_options())
#pp.pprint(x_10.major_holders())
