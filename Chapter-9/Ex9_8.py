#!/usr/bin/env python3
def palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False


if __name__ == '__main__':
	for i in range(000000, 999998):
		if palindrome(str(i).rjust(6, '0')[2:]):
			if palindrome(str(i+1).rjust(6, '0')[1:]):
				if palindrome(str(i+2).rjust(6, '0')[0:]):
					print('%06d' % i)
