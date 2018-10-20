"""
对我来说最难的不是程序，而是命名，真的烦
很多单词我认识但是写不出也想不到，如果有学弟学妹看到了，一定要学好英语！！！
现在很晚了，这道题我已经想到怎么做了，但是很难想命名
所以我选择以数字递增命名，早点写完早点睡觉,我会备注是打印那一部分的.
"""


# '+ - - - -',最小输出单元
# 不会随行列数而变化的,改变边长时改变字符串'- '拼接次数
# end前面的逗号不会自动转换成空格输出
# 其他逗号会自动转换成空格输出
def one_print():
    print('+', '- ' * 4, end='')


# '|        ',最小输出单元
# 不会随行列数而变化的,改变边长时改变空格拼接次数
def two_print():
    print('|', ' '*8, end='')


# 输出类似第一行的一整行+---+----+
# 改变列数需要改变内部函数重复次数,重复columns次
def edge_one_print():
    one_print()
    one_print()
    print("+")


# 输出类似第二行的一整行|    |    |
# 改变列数需要改变内部函数重复次数,重复columns次
def edge_two_print():
    two_print()
    two_print()
    print("|")


# 完成grid画图
# 改变行数需要改变内部函数重复次数,重复rows次
def print_grid():
    part_print()
    part_print()
    edge_one_print()


# 输出像倒着的“山”字的那一部分,2X2中为上半部分
# 不会随着行列数变化的,改变边长时改变内部函数重复次数
def part_print():
    edge_one_print()
    edge_two_print()
    edge_two_print()
    edge_two_print()
    edge_two_print()


# rows = int(input("How many rows do you want to print:"))
# columns = int(input("How many columns do you want to print:"))
print_grid()
