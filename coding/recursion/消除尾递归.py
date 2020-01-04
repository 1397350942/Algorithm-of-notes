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


def recsum(x):
    '''
    比如 求 1 2 3 4 5 的和
    普通递归
    '''
    if x == 1:
        return x
    else:
        return x + recsum(x-1)


def tail_rec_sum(x, running_total=0):
    """
    比如 求 1 2 3 4 5 的和
    尾递归
    """

    if x == 0:
        return running_total
    else:
        return tail_rec_sum(x-1, running_total+x)


"""
1.  tail_rec_sum(5,0)
2.  tail_rec_sum(4,5)
3.  tail_rec_sum(3,9)
4.  tail_rec_sum(2,12)
5.  tail_rec_sum(1,14)
6.  tail_rec_sum(0,15)
"""


def sum(x):
    """消除尾递归"""
    running_total = 0
    while x > 0:
        running_total += x
        x -= 1
    return running_total


"""
逆序
[1,2,3,4,5]
[5,4,3,2,1]
"""


def reverse(s, start, stop):
    """尾递归版的逆序算法"""
    if start < stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start+1, stop-1)
    return s


def reverse_iterative(s):
    """消除逆序算法的尾递归"""
    start, stop = 0, len(s)
    while start < stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        start, stop = start+1, stop-1
    return s


if __name__ == '__main__':
    # print(fib(12, 0, 1))
    # print(recsum(5))
    # print(tail_rec_sum(5))
    # print(sum(5))
    # print(reverse([1, 2, 3, 4, 5, 6], 0, len([1, 2, 3, 4, 5, 6])))
    print(reverse_iterative([5, 4, 3, 2, 1]))
    pass
