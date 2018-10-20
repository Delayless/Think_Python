def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')


a = int(input('请输入a的值'))
b = int(input('请输入b的值'))
c = int(input('请输入c的值'))
n = int(input('请输入n的值'))
check_fermat(a, b, c, n)
