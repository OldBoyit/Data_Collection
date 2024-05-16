import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del sito web contenente i dati di entrate di GameStop
url = "https://finance.yahoo.com/quote/GME/financials?p=GME"

# Effettua la richiesta al sito web
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table')
revenue_table = tables[0]

revenue_data = []
for row in revenue_table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    revenue_data.append([ele for ele in cols if ele])


gme_revenue = pd.DataFrame(revenue_data[1:], columns=revenue_data[0])
print(gme_revenue.tail())

gme_revenue.to_csv('gme_revenue.csv', index=False)
