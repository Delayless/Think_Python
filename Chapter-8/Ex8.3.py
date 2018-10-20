#!usr/bin/env python3

def is_palindrome(arg_num):
    if arg_num == arg_num[::-1]:
        return True
    else:
        return False


while True:
	print(is_palindrome(input('Please input the string:')))

