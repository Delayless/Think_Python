#!/usr/bin/env python3
# coding:utf-8


def triple_tap(string):
    i = 0
    if len(string) < 6:
        return False
    # 最大的i为长度len(str)-6,从0开始的
    while i < len(string) - 5:
        if string[i:i + 6:2] == string[i + 1:i + 7:2]:
            return True
        i = i + 1

    return False


if __name__ == '__main__':
    fin = open('/home/lenovo/Desktop/printpy/Chapter-9/words.txt')
    for letter in fin:
        if triple_tap(letter.strip()):
            print(letter.strip())
