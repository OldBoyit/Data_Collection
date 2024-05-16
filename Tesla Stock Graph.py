import yfinance as yf
import matplotlib.pyplot as plt

tesla_data = yf.download('TSLA')

tesla_data.reset_index(inplace=True)
print(tesla_data.head())

def make_graph(stock_data, title):
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(tesla_data, 'Tesla Stock Price Over Time')
