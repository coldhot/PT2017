import io
name = None
surname = None
with open('settings.txt', 'r') as file:
	lines = file.readlines()
	if len(lines) > 1:
		name = lines[0].replace('\r', '').replace('\n', '')
		surname = lines[1].replace('\r', '').replace('\n', '')
if name is None:
	print("What is your name?")
	name = input()
	print("What is your surname?")
	surname = input()
	with open("settings.txt", "w") as file:
		file.write(name + '\n')
		file.write(surname + '\n')


print("Hello, " + name + ' ' + surname)

print("Write a:")
a = int(input())
print("Write b:")
b = int(input())
print("a + b = " + str(a + b))




settings = {}
settings['name'] = "Dauren"
settings['surname'] = "Yesmukhanov"
settings['friends'] = []
settings['enemies'] = []
person = {}
person['name'] = 'Assel'
settings['enemies'].append(person)
person = {}
person['name'] = 'Timur'
settings['friends'].append(person)

dict2xml(;)