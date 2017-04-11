def get_balance(card_number):
	session = requests.Session()
	r = session.get('https://cabinet.onay.kz/')
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	csrf_token = soup.select('#csrftoken')[0]['value']
	r = session.get('https://cabinet.onay.kz/content/img/SiteLogo.png') 
	my_data = {
		'csrf' : csrf_token,
		'pan': card_number
	}
	headers = {
		''
	    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
		'X-Requested-With':"XMLHttpRequest",
	}
	r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
	result = r.json()
	balance = int(result['result']['balance'])//100
	return balance

def check_card(card_number):
	session = requests.Session()
	r = session.get('https://cabinet.onay.kz/')
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	csrf_token = soup.select('#csrftoken')[0]['value']
	r = session.get('https://cabinet.onay.kz/content/img/SiteLogo.png') 
	my_data = {
		'csrf' : csrf_token,
		'pan': card_number
	}
	headers = {
		''
	    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
		'X-Requested-With':"XMLHttpRequest",
	}
	r = session.post('https://cabinet.onay.kz/check', data = my_data, headers = headers)
	result = r.json()
	return result['type']



