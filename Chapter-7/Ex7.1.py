#!/usr/bin/env python3	
import math


def mysqrt(a, x):
	y = (x + a/x) / 2
	if abs(y-x) < 0.0000001:
		return y
	return mysqrt(a, y)


def test_squre_root():
	print('a		mysqrt		math.sqrt		diff')
	print('-		------		---------		----')
	for i in range(1, 10):
		print('%.1f		%.11f	%.11f		%.11f' % (i, mysqrt(i, i/2), math.sqrt(i), mysqrt(i, i/2)-math.sqrt(i))) 


test_squre_root()

