#!/usr/bin/env python3
import random


def nest_sum(t):
	"""
	Ex10.1
		管他嵌套了多少层,求列表所有元素的和
	"""
	total = 0
	for nested in t:
		if type(nested) == list:
			# 递归求和
			total += nest_sum(nested)
		else:
			total += nested

	return total


def cumsum(t):
	"""
	Ex10.2
		并返回累加和；即一个新列表，其中第 i+1 个元素是原列表中前 i 个元素的和
	"""
	new_list = []
	for i in range(len(t)):
		new_list.append(nest_sum(t[:i+1]))

	return new_list


def middle(t):
	"""
	Ex10.3
		并返回一个除了 第一个和最后一个元素的列表
	"""
	return t[1:-1]


def chop(t):
	"""
		Ex10.4
		删除首尾元素
	"""
	del t[0]
	del t[-1]
	return None

	
def is_sorted(t):
	"""
	Ex10.5
		判断是不是顺序排列
		不能对嵌套的程序运行
	"""
	# sorted是函数,不是list的attributes
	return t == sorted(t)


def is_anagram(word1, word2):
	"""
	Ex10.6
		判断两个单词是不是只有顺序不一样,用的字母一样
	"""
	return sorted(word1) == sorted(word2)


def has_duplicates(t):
	"""
	Ex10.7
		判断是否有重复的元素,
		有重复返回True
	"""
	a = t[0:]
	a.sort()
	for i in range(len(a)-1):
		if a[i] == a[i+1]:
			return True
	
	return False


def random_birth(n):
	a = []
	for i in range(n):
		a.append(random.randint(1,366))
	
	return a


if __name__ == '__main__':
	a = [1, [32, [4, 6, 4, 6], [5, 2]], 4]
	b = [1, 7, 3, 4, 6]
	print(is_sorted(b))
	print(nest_sum(a))
	print(cumsum(a))
	print(is_anagram('aklsjf','aslkjf'))
	c = random_birth(27)
	print(c)
	print(has_duplicates(c))
		
