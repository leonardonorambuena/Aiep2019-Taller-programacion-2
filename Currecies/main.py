import requests
from bs4 import BeautifulSoup
import json
from datetime import date
import os.path
import csv
response = requests.get('https://www.bci.cl/personas/indicadores.json')
data = response.json()
container_indicators = data['kpis']
currencies = []
current_date = str(date.today())

for indicator in container_indicators:
  if indicator['code'] != 'IPSA':
    indicator['date'] = current_date
    currencies.append(indicator)

currencies_filename = 'currencies{}.csv'.format(current_date)

if os.path.isfile(currencies_filename):
  print('Ya se han guardado los registros del {} con anterioridad'.format(current_date))
else:
  with open(currencies_filename, 'w', newline='') as f:
    fieldnames = ['code', 'title', 'trend', 'price', 'date']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    for currency in currencies:
      csv_writer.writerow(currency)
  



