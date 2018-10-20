import turtle


def koch(t, x):
	if x < 3:
		bob.fd(x)
		return
	koch(t, x/3)
	t.lt(60)
	koch(t, x/3)
	t.rt(120)
	koch(t, x/3)
	t.lt(60)
	koch(t, x/3)


def snowflake(t, length):
	for i in range(3):
		koch(t, length)
		t.rt(120)


bob = turtle.Turtle()
snowflake(bob, 120)
turtle.done()
