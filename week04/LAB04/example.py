import requests 
from b4 import BeautifulSoup

url = "http://kurstenge.kz"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("#content table table tr")
for tr in rows:
	print(tr.text)
