import requests
from bs4 import BeautifulSoup
import urllib

def run():
  url = 'https://xkcd.com/'
  for i in range(1, 6):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.content, 'html.parser')
    img_container = soup.find(id = 'comic')
    img_url = img_container.find('img')['src']
    img_name = img_url.split('/')[-1]
    print('descargando la imagen {} en el sistema'.format(img_name))
    # guardar imagen en nuestro sistema
    urllib.request.urlretrieve('https:{}'.format(img_url), img_name)

if __name__ == '__main__':
  run()