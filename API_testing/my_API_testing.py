import pandas_datareader.data as web
prices = web.DataReader('KGH', 'stooq')
print(prices)

