import requests 
session = requests.Session()
r = session.get('https://cabinet.onay.kz/')
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
csrf_token = soup.select('#csrftoken')[0]['value']
my_data = {
	'csrf' : csrf_token,
	'pan': '9643908503307104996'
}
headers = {
	''
    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
	'X-Requested-With':"XMLHttpRequest",
	'Cookie':"_ga=GA1.2.264391765.1486105106; lang=ru; _pk_id.1.4deb=e2af0b39ec6e44cc.1486105145.3.1487925944.1487925944.; _pk_ref.1.4deb=%5B%22%22%2C%22%22%2C1487925944%2C%22https%3A%2F%2Fwww.google.kz%2F%22%5D; PHPSESSID=gf553pd3elp822hvkj1bg6hsd7; _pk_ses.1.4deb=*"
}
r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
print(r.text)