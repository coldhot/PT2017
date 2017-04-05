from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup


def f(x):
	return x*x

def parse_page(page):
	url = "https://www.olx.kz/elektronika/telefony-i-aksesuary/?page=%d" % page
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	prices = soup.select('#offers_table p.price strong')
	total_prices = 0
	for p in prices:
		text = p.text
		np = []
		for s in text:
			if s.isdigit():
				np.append(s)
		if len(np) == 0:
			continue
		n = int("".join(np))
		total_prices = total_prices + n
	return total_prices

if __name__ == '__main__':
    pool = Pool(processes=8)              # start 4 worker processes
    l = pool.map(parse_page, range(1, 500))
    s = 0
    for item in l:
    	s = s + item
    print(s)