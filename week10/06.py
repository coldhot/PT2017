from multiprocessing import Pool

def f(x):
	return x*x

if __name__ == '__main__':
    pool = Pool(processes=8)
    l = pool.map(f, range(1, 5000000))
    print(l)