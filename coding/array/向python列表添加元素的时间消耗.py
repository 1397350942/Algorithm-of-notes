import sys
from time import time

maxN = 10000000


def compute_average(n):
    """返回添加元素的平均时间"""
    data = []
    start = time()
    for i in range(n):
        data.append(i)
    end = time()
    return (end - start)/n


if __name__ == "__main__":
    n = 10
    while n <= maxN:
        print("平均时间:{0:.3f} n:{1}".format(compute_average(n)*1000000, n))
        n *= 10
