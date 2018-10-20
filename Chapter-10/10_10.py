#!/usr/bin/env python3
import bisect as bi


def make_words_list_append():
    fin = open('words.txt')
    a = []
    for line in fin:
        a.append(line.strip())
	return a

def in_bisect(word_list, word):
	if len(word_list) == 0:
		return False
	
	medium = len(word_list) // 2
	if word_list[medium] == word:
		return True
	
	if word_list[medium] < word
		return in_bisect(word_list[medium+1:])
	else:
		return in_bisect(word_list[:medium])
				
def in_bisect_cheat(word_list, word)

