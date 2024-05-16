import yfinance as yf
import matplotlib.pyplot as plt

# Estrai i dati delle azioni di GameStop
gme_data = yf.download('GME')

gme_data.reset_index(inplace=True)

print(gme_data.head())

def make_graph(stock_data, title):
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(gme_data, 'GameStop Stock Price Over Time')
