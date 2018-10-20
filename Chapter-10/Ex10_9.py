#!/usr/bin/env python3
import time


def make_words_list_append():
	fin = open('words.txt')
	a = []
	for line in fin:
		a.append(line.strip())


def make_words_list_plus():
	fin = open('words.txt')
	# fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')
	a = []
	for line in fin:
		a += [line.strip()]


def main():
	start_time = time.time()
	make_words_list_append()
	print('append spend times: %f'% (time.time()-start_time))
	start_time = time.time()
	make_words_list_plus()
	print('plus spend times: %f' % (time.time()-start_time))


if __name__ == '__main__':
	main()

