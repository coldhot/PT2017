import requests 
from bs4 import BeautifulSoup

url = "http://kurstenge.kz"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("#content table table tr")[:3]
for tr in rows:
	name = tr.select("td a")[0].text
	rate = float(tr.select("td span.today")[0].text.replace(",", "."))
	print("%s\t%f" % (name, rate))

