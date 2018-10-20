#!/usr/bin/env python3


def is_abecedarian(word):
    for i in range(len(word) - 1):
        # 如果前一个字母比后一个字母大就返回False
        if word[i] > word[i + 1]:
            return False

    return True


fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')
for line in fin:
    if is_abecedarian(line.strip()):
        print(line.strip())
