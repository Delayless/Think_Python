#!/usr/bin/env python3
from Ex9_4_text import * 

def uses_all(word, string):
	return uses_only(string, word)


if __name__ == '__main__':
	fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')	
	for letter in fin:
		if uses_all(letter.strip(), 'aeiou'):
			print(letter.strip())
