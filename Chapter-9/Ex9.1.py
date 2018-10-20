#!/usr/bin/env python3

fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')
for line in fin:
	if len(line.strip()) > 20:
		print(line)

