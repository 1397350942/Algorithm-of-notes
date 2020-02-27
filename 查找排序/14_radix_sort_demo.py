def radix_sort(dataset):
    """基数排序"""
    max_num = max(dataset)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 创建空桶
        for var in dataset:
            """分桶"""
            digit = (var // (10 ** it)) % 10
            buckets[digit].append(var)
        dataset.clear()
        for buc in buckets:
            dataset.extend(buc)
        it += 1

# def radix_sort_test(li):
#     max_num = max(li)  # 最大值 9->1, 99->2, 888->3, 10000->5
#     it = 0
#     while 10 ** it <= max_num:
#         buckets = [[] for _ in range(10)]
#         for var in li:
#             # 987 it=1  987//10->98 98%10->8;    it=2  987//100->9 9%10=9
#             digit = (var // 10 ** it) % 10
#             buckets[digit].append(var)
#         # 分桶完成
#         li.clear()
#         for buc in buckets:
#             li.extend(buc)
#         # 把数重新写回li
#         it += 1


# def radix_sort(dataset):
#     """基数排序"""
#     max_num = max(dataset)
#     it = 0
#     while 10 ** it <= max_num:
#         buckets = [[] for _ in range(10)]  # 创建空桶
#         for var in dataset:
#             """分桶"""
#             digit = (var // (10 ** it)) % 10
#             buckets[digit].append(var)
#         dataset.clear()
#         for buc in buckets:
#             """把桶里面的数重新写回dataset里面"""
#             dataset.extend(buc)
#         it += 1

if __name__ == "__main__":
    import random
    dataset = list(range(1000))
    random.shuffle(dataset)
    radix_sort(dataset)
    print(dataset)
