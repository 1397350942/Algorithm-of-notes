def count_sort(dataset, max_count=100):
    """计数排序"""
    count = [0 for _ in range(max_count+1)]
    for val in dataset:
        count[val] += 1
    dataset.clear()
    for ind, val in enumerate(count):
        for _ in range(val):
            dataset.append(ind)


if __name__ == "__main__":
    dataset = [1, 2, 4, 1, 2, 6, 7, 1]
    print(dataset)
    count_sort(dataset)
    print(dataset)

# def count_sort(dataset, max_count=100):
#     """计数排序"""
#     count = [0 for _ in range(max_count+1)]
#     for val in dataset:
#         count[val] += 1
#     dataset.clear()
#     for ind, val in enumerate(count):
#         for i in range(val):
#             dataset.append(ind)


# if __name__ == "__main__":
#     dataset = [1, 2, 4, 2, 1, 5]
#     print(dataset)
#     count_sort(dataset)
#     print(dataset)
# def count_sort(dataset, max_count=100):
#     """计数排序"""
#     count = [0 for _ in range(max_count+1)]
#     # print(count)
#     for value in dataset:
#         count[value] += 1
#     dataset.clear()
#     for index, value in enumerate(count):
#         for i in range(value):
#             dataset.append(index)
# if __name__ == "__main__":
#     dataset = [1, 3, 2, 4, 1, 2, 3, 1, 3, 5]
#     count_sort(dataset)
#     print(dataset)
# def count_sort(dataset, max_count=100):
#     """计数排序"""
#     count = [0 for _ in range(max_count+1)]

#     for value in dataset:
#         count[value] += 1

#     for index, value in enumerate(count):
#         for i in range(value):
#             dataset.append(index)
# def count_sort(dataset, max_count=100):
#     """计数排序"""
#     count = [0 for _ in range(max_count+1)]
#     for val in dataset:
#         count[val] += 1
#     dataset.clear()
#     for ind, val in enumerate(count):
#         for i in range(val):
#             dataset.append(ind)

# if __name__ == "__main__":
#     dataS = [1, 3, 2, 4, 5, 1, 2, 1, 3]
#     print(dataS)
#     count_sort(dataS)
#     print(dataS)
