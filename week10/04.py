import threading
n = 10000
p = 0
def fact_even():
	global p
	for i in range(2, n + 1, 2):
		p = p + i
		print("fact even: %d" % p)

def fact_odd():
	global p
	for i in range(1, n + 1, 2):
		p = p + i
		print("fact odd: %d" % p)


# init threads
t1 = threading.Thread(target=fact_even)
t2 = threading.Thread(target=fact_odd)

# start threads
t1.start()
t2.start()