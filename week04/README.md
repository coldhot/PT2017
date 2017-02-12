Python Tuples
_____________
A tuple consists of a number of values separated by commas. They are useful for ordered pairs and returning several values from a function.

creation: 

		 		emptyTuple = ()

		  		singleItemTuple = (“spam”,)

          		thistuple = 12, 89, ‘a’

          		thistuple = (12, 89, ‘a’)



accessing: 

				thistuple[0] returns 12

		  		a, b, c = thistuple returns a = 12, b = 89, c = ‘a’


Python Dictionaries
__________________
A dictionary is a set of key:value pairs. All keys in a dictionary must be unique.
creation:

				emptyDict = {}
 				
 				thisdict = {‘a’:1, ‘b’:23, ‘c’:”eggs”}

accessing: 

				thisdict[‘a’] returns 1 


deleting: 

				del thisdict[‘b’]

finding:
 

				thisdict.has_key(‘e’)	returns False
	
				thisdict.keys()			returns [‘a’, ‘c’]

				thisdict.items()		returns [(‘a’, 1), (‘c’, ‘eggs’)]

				‘c’ in thisdict			returns True

				‘abce’ in thisdict		returns False


Python Lists
_____________

One of the most important data structures in Python is the list.  Lists are very ﬂexible and have many built-in control functions.

creation:

				thelist = [5,3,‘p’,9,‘e’]


accessing:
				
				thelist[0]				returns 5

slicing:
				
				thelist[1:3]			returns [3, ‘p’]

				thelist[2:]				returns [‘p’, 9, ‘e’]

				thelist[:2]				returns [5, 3]

				thelist[2:-1]			returns [‘p’, 9]

length:

				len(thelist)			returns 5

sort:
				
				thelist.sort()			no return value

add:

				thelist.append(37)

remove & return:

				thelist.pop()			returns 37

				thelist.pop(1)			returns 5

insert:

				thelist.insert(2, ‘z’)

remove:

				thelist.remove(‘e’)

				del thelist[0]


concatenation: 

				thelist + [0]			returns [‘z’,9,’p’,0]

ﬁnding:

				9 in thelist			returns True
