#!/usr/bin/env python3


def gcd(aa, bb):
	if bb == 0:
		return aa
	r = aa % bb
	return gcd(bb, r)


a = int(input("Please input a number:"))
b = int(input("Please input another number:"))
print('The greatest common divisor,GCD is  %d' % gcd(a, b))
