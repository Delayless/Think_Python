def is_triangle(a, b, c):
    if a+b > c and b+c > a and a+c > b:
        print('Yes')
    elif a+b == c or b+c == a or a+c == b:
        print("退化三角形")
    else:
        print('No')


while True:
    a = int(input('请第一根棍子的长:'))
    b = int(input('请第二根棍子的长:'))
    c = int(input('请第三根棍子的长:'))
    is_triangle(a, b, c)
