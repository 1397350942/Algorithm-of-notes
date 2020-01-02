# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""
"""
递归的基本思想 

step1: (n-1)假设,需要假设较小规模的计算已经完成 
step2: 利用已知和假设计算未知 
step3: 确定结束条件
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



