# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""

bad_count = 0
good_count = 0


def bad_fibonacci(n):
    global bad_count
    bad_count += 1
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


def good_fibonacci(n):
    global good_count
    good_count += 1
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)


print(bad_fibonacci(12))
print(good_fibonacci(12))
print(bad_count)
print(good_count)
