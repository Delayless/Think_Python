def recurse(n, sum_0toN=0):
    """
    求0到n的和,放在s中,并print出来
    s初始值为0
    :param n:
    :param sum_0toN:
    :return:
    """
    if n == 0:
        print(sum_0toN)
    else:
        recurse(n-1, n+sum_0toN)


recurse(-1, 0)
