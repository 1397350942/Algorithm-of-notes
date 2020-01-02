# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
description: None
"""
"""
尾递归要满足的条件:
1. 占用了常量的栈空间
2. 在函数中只是单纯调用函数本身
3. 需要在函数最后调用函数本身 
4. 调用需要是线性的 
5. 需要调用一次
"""


def fib(n, n1, n2):
    """尾递归版的斐波那契数列"""
    if n == 0:
        return n1
    return fib(n - 1, n2, n1 + n2)


if __name__ == '__main__':
    print(fib(12, 0, 1))
