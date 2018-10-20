#!/usr/bin/env python3	

while True:
	str_input = input('Please input the mathematic expression:')
	if str_input == 'done':
		break
	print(eval(str_input))
