QUIZ #1 
=============


1.	What gets printed? Assuming python version 3.x:
			
			print(1/2)


2.	What is the output of the below program?
	
			a = [1,2,3,None,(),[],]
			print(len(a))


3.	What gets printed?

			x = 4.5
			y = 2
			print(x//y)

4.	What gets printed?
			
			nums = set([1,1,2,3,3,3,4])
			print(len(nums))

5.	What gets printed?

			x = True
			y = False
			z = False

			if x or y and z:
				print("yes")
			else:
				print("no")

6.	What gets printed?

			x = True
			y = False
			z = False

			if not x or y:
				print(1)
			elif not x or not y and z:
				print(2)
			elif not x or y or not y and x:
				print(3)
			else:
				print(4)

7.	What gets printed?

			name = "snow storm"
			print(name[6:8])

8.	What gets printed?

			name = "snow storm"
			name[5] = 'X'
			print(name)

9.	Which of the following print statements will print all the names in the list on a seperate line
	
			names = ['Ramesh', 'Rajesh', 'Roger', 'Ivan', 'Nico']

	* print "\n".join(names)
	* print names.join("\n")
	* print names.concatenate("\n")
	* print names.append("\n")
	* print names.join("%s\n", names)

10.	What gets printed?
	
			country_counter = {}

			def addone(country):
			    if country in country_counter:
			        country_counter[country] += 1
			    else:
			        country_counter[country] = 1

			addone('China')
			addone('Japan')
			addone('china')

			print(len(country_counter))

11.	What gets printed?
			
			confusion = {}
			confusion[1] = 1
			confusion['1'] = 2
			confusion[1] += 1

			sum = 0
			for k in confusion:
			    sum += confusion[k]

			print(sum)

12.	What gets printed?

			boxes = {}
			jars = {}
			crates = {}

			boxes['cereal'] = 1
			boxes['candy'] = 2
			jars['honey'] = 4
			crates['boxes'] = boxes
			crates['jars'] = jars

			print(len(crates[boxes]))

13.	What gets printed?

			names = ['Nursultan', 'Dariga', 'Rakhat', 'Karim']
			print(names[-1][-1])

14.	What gets printed?
			a = 1
			b = 2
			a,b = b,a

			print("%d %d" % (a,b))

15. Write regex for credit cards.

	All Visa card numbers start with a 4. New cards have 16 digits.

	MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.

