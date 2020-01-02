# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)



