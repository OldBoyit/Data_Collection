import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.yahoo.com/quote/TSLA/financials?p=TSLA"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table')
revenue_table = tables[0]

# Estrai i dati dalla tabella
revenue_data = []
for row in revenue_table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    revenue_data.append([ele for ele in cols if ele])

# Crea un dataframe
tesla_revenue = pd.DataFrame(revenue_data[1:], columns=revenue_data[0])

# Visualizza le ultime cinque righe del dataframe
print(tesla_revenue.tail())

tesla_revenue.to_csv('tesla_revenue.csv', index=False)
