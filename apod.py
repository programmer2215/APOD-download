from bs4 import BeautifulSoup as soup
from urllib.request import urlretrieve
import requests as req
from datetime import date

today = date.today().strftime("%d-%m-%Y")

url = 'https://apod.nasa.gov/apod/astropix.html'


with open('log.txt', 'r') as fh:
    last_update = fh.read()
    if str(today) > last_update or len(last_update) < 1:
        request = soup(req.get(url).content, 'html.parser')
        a = request.find_all('a')
        b = a[1]
        v = 'https://apod.nasa.gov/apod/' + b.get('href')
        val = urlretrieve(v,str(today)+'.jpeg')
        fh.close()
        with open('log.txt', 'w') as fh:
            fh.write(str(today))
            fh.close()
    else:
        print('upto date!!!')


