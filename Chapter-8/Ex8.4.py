#!/usr/bin/env python3

def rotate_word(str_cypher, offset):
	i = 0
	plain = ''
	for letter in str_cypher:
		plaintext_temp = ord(letter) + offset
		# if 'a' < letter < 'z':
		if letter.islower():
		# -2%26 == 24
		# 答案的方法就是跟a(或A)的偏差求余,再加上a或者A的ascii码值就可以了
			if plaintext_temp > ord('z'): 
				plaintext_temp = plaintext_temp - 26
			if plaintext_temp < ord('a'): 
				plaintext_temp = plaintext_temp + 26

		# if 'A' < letter < 'Z':
		if letter.isupper():
			if plaintext_temp > ord('Z'): 
				plaintext_temp = plaintext_temp - 26
			if plaintext_temp < ord('A'): 
				plaintext_temp = plaintext_temp + 26

		plain += chr(plaintext_temp)

	return plain


while True:
	password = input('Please input a string to Decryption:')
	offset_num = int(input('Offset:'))
	print(rotate_word(password, offset_num))

