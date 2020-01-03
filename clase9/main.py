import requests
from bs4 import BeautifulSoup
from datetime import date


url = 'https://www.bcentral.cl/web/banco-central/inicio'

response = requests.get(url, verify = False)

if response.status_code == 200:
  class_indicators = 'indicators-blocksecondinner'
  soup = BeautifulSoup(response.content, 'html.parser')

  containers = soup.find_all(class_='indicators-blocksecondinner')

  for container in containers:
    colindicators = containers.find_all('dl')
    for colindicator in colindicators:
      print(colindicator)


