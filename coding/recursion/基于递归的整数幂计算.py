# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""
"""
n^5 = n * n * n * n * n = n * n ^ 4 
n^m = n * n^(m-1)
"""


def power(a, n):
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)


def power_ext(a, n):
    """
    减低消耗
    a^10 = a^5 *a^5
    a^11 = a * a^5 * a^5
    """
    y = 0
    if n == 0:
        y = 1
    else:
        y = power(a, n // 2)
        y = y * y
        if n % 2 == 1:
            y = y * a
    return y


if __name__ == '__main__':
    print("2^10==>{}".format(power(2, 10)))
    print("2^10==>{}".format(power_ext(2, 10)))
