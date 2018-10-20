#!/usr/bin/env python3

def has_no_e():	
	fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')
	for line in fin:
		if line.strip().find('e') == -1:
			print(line)


has_no_e()

