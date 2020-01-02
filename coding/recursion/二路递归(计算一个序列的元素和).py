# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""
"""
s = [1,5,6,8,3]
"""


def binary_sum(s, start, stop):
    """使用二路递归计算序列元素之和"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)


def sum(s, start, stop):
    """使用单路递归计算序列元素之和"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        return s[start] + sum(s, start + 1, stop)


if __name__ == '__main__':
    s = [1, 5, 6, 8, 3]
    print(binary_sum(s, 0, len(s)))
    print(sum(s, 0, len(s)))
