import math


def is_palindrome(word):
	for i in range(len(word)):
		if not word[i] == word[-1-i]:
			return False
		elif i == len(word)//2 or i == len(word)/2-1:
			return True 
	
while True:
	print (is_palindrome(input("Please input a string for checking is palindrome or not\n")))

