#!usr/bin/env python3
import math


def factorial(k):
	if k == 0:
		return 1
	return k*factorial(k-1)
	

def estimate_pi():
	k = 0
	total = 0
	term = 0
	proportion = 2 * math.sqrt(2)/9801
	while True:
		term = proportion * (factorial(4*k) * (1103 + 26390*k))/(((factorial(k))**4)*396**(4*k))
		total += term
		if term < 1e-15:
			break
		k += 1
	return 1/total


print(estimate_pi())


