# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""


def binary_search_recursion(data, target, low, high):
    """
    二分查找(递归)
    如果找到,返回True,未找到,返回False
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:  # 找到target
            return True
        elif target < data[mid]:  # 在mid左侧
            return binary_search_recursion(data, target, low, mid - 1)
        else:  # 在mid右侧
            return binary_search_recursion(data, target, mid + 1, high)


def binary_search(data, target):
    # [10, 20, 30, 40, 50, 60]
    return binary_search_recursion(data, target, 0, len(data) - 1)


if __name__ == '__main__':
    print(binary_search([10, 20, 30, 40, 50, 60], 20))
