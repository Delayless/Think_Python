import turtle
# length_all = float(input("Please input length:"))


# 走一条直线再左转九十度
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
# 可以画5次
for j in range(5):
    square(bob, float(input("Please input length:")))
turtle.done()
