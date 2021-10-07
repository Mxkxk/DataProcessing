__doc__ = "Module with functions for basic sequences"
def fibonacci(n):
	fibonacciSeq = [0, 1]	
	for i in range(n):
		fibonacciSeq.append(fibonacciSeq[-1]+fibonacciSeq[-2])
	return fibonacciSeq
#n - start digit, d - step, m - ammount of sequence (a...a+(m-1)*d)
def arithmetic(n, d, m):
	arithmeticSeq = [n+i*d for i in range(m)]
	return arithmeticSeq
#n - start digit, r - step, m - ammount of sequence (a...ar^m)
def geometric(n, r, m):
	geometricSeq = [n*(r**i) for i in range(m)]
	return geometricSeq
#n - start digit(n!=0), d - step, m - ammount of sequence (1/a...1/(n+i*d))
def harmonic(n, d, m):
	if n != 0:
		harmonicSeq = [1/(n+i*d) for i in range(m)]
		return harmonicSeq