def sift(dataset, low, high):
    """
    :param dataset: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置 
    :return 
    """
    i = low  # i最开始指向的根节点
    j = 2 * i + 1  # j开始时左孩子
    tmp = dataset[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and dataset[j+1] > dataset[j]:
            j = j + 1  # j指向右孩子
        if dataset[j] > tmp:
            dataset[i] = dataset[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大,把tmp放到i的位置上
            dataset[i] = tmp
            break
    else:
        dataset[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(dataset):
    n = len(dataset)
    for i in range((n-2)//2, -1, -1):
        # i 表示建堆的时候调整的部分的根的下标
        sift(dataset, i, n-1)
    for i in range(n-1, -1, -1):
        # i 指向当前堆的最后一个元素
        dataset[0], dataset[i] = dataset[i], dataset[0]
        sift(dataset, 0, i-1)


if __name__ == "__main__":
    dataset = [6, 8, 1, 9, 3, 0, 7, 2, 4, 5]
    heap_sort(dataset)
    print(dataset)


# def sift(dataset, low, high):
#     i = low
#     j = 2 * i + 1
#     tmp = dataset[low]
#     while j <= high:
#         if j+1 <= high and dataset[j+1] > dataset[j]:
#             j = j + 1
#         if dataset[j] > tmp:
#             dataset[i] = dataset[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             dataset[i] = tmp
#             break
#     else:
#         dataset[i] = tmp


# if __name__ == "__main__":
#     dataset = [6,8,1,9,3,0,7,2,4,5]
#     print(dataset)
#     sift(dataset,0,len(dataset)-1)
#     print(dataset)


# def sift(dataset, low, high):
#     i = low  # i为最开始的根节点
#     j = 2 * i + 1  # 左孩子
#     tmp = dataset[low]
#     while j <= high:
#         if j+1 <= high and dataset[j+1] > dataset[j]:
#             j = j+1
#         if dataset[j] > tmp:
#             dataset[i] = dataset[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             dataset[i] = tmp
#             break
#     else:
#         dataset[i] = tmp

# def sift(dataset, low, high):
#     i = low  # i最开始指向根节点
#     j = 2 * i + 1  # j最开始指向左孩子
#     tmp = dataset[low]  # 把堆顶存起来
#     while j <= high:  # 只要j位置有数
#         if j+1 <= high and dataset[j+1] > dataset[j]:
#             """如果右孩子存在,且比左孩子大"""
#             j = j + 1  # j 指向右孩子
#         if dataset[j] > tmp:
#             dataset[i] = dataset[j]
#             i = j
#             j = 2 * i + 1
#         else:  # tmp更大,把tmp放到i的位置上
#             dataset[i] = tmp
#             break
#     else:
#         # 把tmp放到叶子节点上
#         dataset[i] = tmp


# def sift(dataset, low, high):
#     i = low  # i最开始指向根节点
#     j = 2 * i + 1  # j最开始指向左孩子
#     tmp = dataset[low]  # 把堆顶存起来
#     while j <= high:  # 只要j位置有数
#         if j+1 <= high and dataset[j+1] > dataset[j]:
#             """如果右孩子存在,并且比做孩子大"""
#             j = j + 1  # j指向右孩子
#         if dataset[j] > tmp:
#             dataset[i] = dataset[j]
#             i = j
#             j = 2 * i + 1
#         else:  # tmp更大,把tmp放到i的位置上
#             dataset[i] = tmp
#             break
#     else:
#         # 把tmp放到叶子节点上
#         dataset[i] = tmp


# def sift(dataset, low, high):
#     """
#     :param dataset:列表
#     :param low:堆的根节点位置
#     :param high:堆的最后一个元素
#     :return
#     """
#     i = low  # i最开始指向根节点
#     j = 2 * i + 1  # j最开始指向左孩子
#     tmp = dataset[low]  # 把堆顶存起来
#     while j <= high:  # 只要j位置有数
#         if j+1 <= high and dataset[j+1] > dataset[j]:  # 如果右孩子存在,并且比左孩子大
#             j = j + 1  # j指向右孩子
#         if dataset[j] > tmp:
#             dataset[i] = dataset[j]
#             i = j
#             j = 2 * i + 1
#         else:  # tmp更大,把tmp放到i的位置上
#             dataset[i] = tmp  # 把tmp放到某一级领导位置上
#             break
#     else:
#         dataset[i] = tmp # 把tmp放到叶子节点上
