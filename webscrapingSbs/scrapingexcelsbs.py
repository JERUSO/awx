from bs4 import BeautifulSoup as bs
import requests

DOMAIN = "https://www.sbs.gob.pe"
URL = "https://intranet2.sbs.gob.pe/estadistica/financiera/2021/Febrero/"
FILETYPE ='.XLS'

def get_soup(url):
    return bs(requests.get(url).text,'html.parser')

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
      print(file_link)
