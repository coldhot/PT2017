import json

settings = {}
settings['name'] = "Dauren"
settings['surname'] = "Yesmukhanov"
settings['friends'] = []
settings['enemies'] = []
person = {}
person['name'] = 'Assel'
settings['enemies'].append(person)
person = {}
person['name'] = 'Rashida'
settings['enemies'].append(person)
person = {}
person['name'] = 'Timur'
settings['friends'].append(person)
person = {}
person['name'] = 'Iskander'
settings['friends'].append(person)

s = json.dumps(settings)
with open("temp.json", "w") as file:
	file.write(s)

with open("temp.json", "r") as file:
	lines = file.readlines()
	print(json.loads(lines[0]))