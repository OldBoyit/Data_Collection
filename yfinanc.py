import yfinance as yf
import pandas as pd

tesla_data = yf.download('TSLA')

tesla_data.reset_index(inplace=True)

tesla_data.to_csv('tesla_data.csv', index=False)

print(tesla_data.head())