import requests
import csv
from datetime import date
import os.path

response = requests.get('https://www.bci.cl/personas/indicadores.json')

if response.status_code != 200:
  print('Error obteniendo los datos estado {}'.format(response.status_code))

json_response = response.json()

indicators = json_response['kpis']

data = []

for indicator in indicators:
  if indicator['code'] == 'UF':
    data.append(indicator)
  if indicator['code'] == 'USD':
    data.append(indicator)

file_name = 'indicadores{}.csv'.format(str(date.today()))

if os.path.isfile(file_name):
  print('Ya existe un registro con fecha {}'.format(str(date.today())))

else:
  with open(file_name, 'w', newline= '') as f:
    file_csv = csv.writer(f)
    file_csv.writerow(['Indicador', 'Valor'])
    for d in data:
      file_csv.writerow([d['code'], d['price']])
