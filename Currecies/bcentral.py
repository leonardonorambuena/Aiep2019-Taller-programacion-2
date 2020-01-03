import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

def write_csv(columns, values):
    if len(columns) != len(values):
        raise Exception('Las columnas no contienen la misma cantidad de datos')

    file_name = 'bcentral-indicadores{}.csv'.format(str(date.today()))
    with open(file_name, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(columns)
        for val in values:
            csv_writer.writerow(val.values())


def run():
    url = 'https://www.bcentral.cl/web/banco-central/inicio'

    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.content, 'html.parser')

    containers = soup.find_all(class_='indicators-blocksecondinner')

    indicators = []

    for container in containers:
        indicators_container = container.find_all('dl')
        for indicator in indicators_container:
            indicator_name = indicator.find('dt', {'class': 'indicators-mainkey'}).get_text()
            if indicator_name != None and indicator_name in ['UF', 'Dólar Observado']:
                indicator_value = float(indicator.find('dd', {'class': 'indicators-value'}).get_text().replace('\n', '').replace('$','').replace('.','').replace(',','.'))
                
                indicators.append({'name' : indicator_name, 'value':indicator_value})

    write_csv(['Indicador', 'Valor'], indicators)
    print(indicators)


if __name__ == '__main__':
    run()