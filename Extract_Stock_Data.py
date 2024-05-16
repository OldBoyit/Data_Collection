import yfinance as yf
import pandas as pd

# Estrai i dati delle azioni di GameStop
gme_data = yf.download('GME')

# Azzerare l'indice
gme_data.reset_index(inplace=True)

# Salvare il dataframe in un file CSV (facoltativo)
gme_data.to_csv('gme_data.csv', index=False)

# Visualizzare le prime cinque righe del dataframe
print(gme_data.head())
