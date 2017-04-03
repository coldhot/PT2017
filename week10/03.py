import threading

x  = 0
def incrementor(foo, event):
	global x
	while True:
		x = x + 1

def check(foo, event):
	global x 
	while True:
		y = x
		if y % 2 == 0:
			print(y)

# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=incrementor, args=(0, e1))
t2 = threading.Thread(target=check, args=(0, e2))

# start threads
t1.start()
t2.start()

e1.set() # initiate the first event
e2.set()

# join threads to the main thread
t1.join()
t2.join()