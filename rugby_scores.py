import numpy
import sys
import matplotlib.pyplot as plt

def number_one_score(n):
	# Computes the number of ways to obtain n points, given the rugby rules:
	# 3 pts for a penalty, 5 pts for a try and 7 pts for a transformed try
	scores = numpy.zeros((n+1,1))
	scores[0] = 1
	additioners = [3, 5, 7]
	#for a in additioners:
	#	scores[a] = 1
	# number k: k = (k-a) + a 
	# scores[k] = \sum_{a in additioners} scores[k-a]
	for k in range(1,n+1):
		for a in additioners:
			if (k-a)>=0:
				scores[k] = scores[k] + scores[k-a] 
	return scores
	
	
def newton(x0,iterations,f,df):
	for k in range(iterations):
		x0 = x0 - f(x0)/df(x0)
	return x0
	

def polynomial_rugby(deriv=True):
	if deriv:
		return lambda x: x**7-x**4-x**2-1
	return lambda x : 7*x**6-4*x**3-2*x

if __name__ == '__main__':
	n = int(sys.argv[1])
	scores = number_one_score(n)
	print(scores)
	
	plt.plot(scores)
	plt.show()
	plt.xlabel("Score")
	plt.ylabel("Number of possibilities")
	
	plt.semilogy(scores)
	plt.show()
	plt.xlabel("Score")
	plt.ylabel("Number of possibilities (Log)")
	
	# scores[k] behaves like r^k with r>1
	# How to find r ?
	
	# Method 1: analytic
	# r^k = \sum_{a in additioners} r^{k-a}
	# r is a root of the polynomial:
	# X^A = \sum_{a in additioners} X^{A-a} with A = max (additioners) 
	# application X^7 = X^4 + X^2 + 1
	
	# Newton method, y= f(x) + hf'(x), vanishes when y = 0, h = - f(x)/f'(x)
	# x_{n+1} = x_n -f(x_n)/f'(x_n)
	
	print("Analytic solution from the rugby polynomial")
	print(newton(2,10,polynomial_rugby(),polynomial_rugby(deriv = False)))
	
	# Method 2: empiric with a linear regression applied to x,log(y)
	x = numpy.reshape(numpy.array([i for i in range(n+1)]),(n+1,1))
	x = numpy.stack((x,numpy.zeros((n+1,1))+1),axis=1)[:,:,0]
	y = numpy.log(scores)
	params = numpy.linalg.lstsq(x,y) 
	print(params)
