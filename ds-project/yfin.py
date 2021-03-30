import yfinance as yf
import pprint

pp = pprint.PrettyPrinter(indent=4)

msft = yf.Ticker("MSFT")
pp.pprint(msft.info)
