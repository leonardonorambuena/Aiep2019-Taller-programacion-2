import requests
from bs4 import BeautifulSoup
import urllib

def run():
  url = 'https://xkcd.com/'
  for i in range(1, 101):
    response = requests.get(url+str(i))
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')

      img_container = soup.find(id='comic')
      img_url = img_container.find('img')['src']
      img_name = img_url.split('/')[-1]
      print('Descargando la imagen {}'.format(img_name))
      urllib.request.urlretrieve('https:{}'.format(img_url), img_name)
    else:
      print('Error no se encontraron más fotos')



if __name__ == '__main__':
  run()