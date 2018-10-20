#!/usr/bin/env python3


def uses_only(word, string):	
	for letter in word:
		if string.find(letter) == -1:
			return False 

	return True


fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')		
for line in fin:
	word = line.strip()	
	if uses_only(word, 'acefhlo'):
		print(word)	

