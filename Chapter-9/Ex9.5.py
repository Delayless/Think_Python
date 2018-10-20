#!/usr/bin/env python3

def uses_all(word, string):
	for letter in string:
		# 如果string里的字母不在word里面就返回-1
		# 即字符串里的每个字母都必须在word里至少出现一次才会返回True
		if word.find(letter) == -1:
			return False

	return True


fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')

i = 0
for line in fin:
	if uses_all(line.strip(), 'aeiou'):
		print(line.strip())
		i = i + 1

print(i)

