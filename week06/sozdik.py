import requests
def translate(word, lang_from = 'ru', lang_to = 'kk'):
	url = "https://sozdik.kz/translate/%s/%s/%s/" % (lang_from, lang_to, word)
	r = requests.get(url)
	data = r.json()
	translation = data['translation']
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(translation, "html.parser")
	l = soup.select("span a")
	result = []
	for item in l:
		result.append(item.text)
	return result

r = translate('ручка', lang_to='kk', lang_from = 'ru')
s = ",".join(r)
print(s)
