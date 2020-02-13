def position(dataset, left, right):
    tmp = dataset[left]
    while left < right:
        while left < right and dataset[right] >= tmp:
            right -= 1
        dataset[left] = dataset[right]
        while left < right and dataset[left] <= tmp:
            left += 1
        dataset[right] = dataset[left]
    dataset[left] = tmp
    return left


def quick_sort(dataset, left, right):
    if left < right:
        mid = position(dataset, left, right)
        quick_sort(dataset, left, mid-1)
        quick_sort(dataset, mid+1, right)


if __name__ == "__main__":
    li = [5, 6, 1, 2, 3, 4, 8, 9]
    quick_sort(li, 0, len(li)-1)
    print(li)
# def position(dataset, left, right):
#     tmp = dataset[left]
#     while left < right:
#         while left < right and dataset[right] >= tmp:
#             right -= 1
#         dataset[left] = dataset[right]
#         while left < right and dataset[left] <= tmp:
#             left += 1
#         dataset[right] = dataset[left]
#     dataset[left] = tmp
#     return left


# def quick_sort(dataset, left, right):
#     if left < right:
#         mid = position(dataset, left, right)
#         quick_sort(dataset, left, mid-1)
#         quick_sort(dataset, mid+1, right)


# if __name__ == "__main__":
#     li = [6, 7, 2, 5, 1, 2]
#     quick_sort(li, 0, len(li)-1)
#     print(li)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def position(dataset, left, right):
#     tmp = dataset[left]
#     while left < right:
#         while left < right and dataset[right] >= tmp:
#             right -= 1
#         dataset[left] = dataset[right]
#         while left < right and dataset[left] <= tmp:
#             left += 1
#         dataset[right] = dataset[left]
#     dataset[left] = tmp
#     return left


# def quick_sort(dataset, left, right):
#     """快速排序"""
#     if left < right:
#         mid = position(dataset, left, right)
#         quick_sort(dataset, left, mid-1)
#         quick_sort(dataset, mid+1, right)


# if __name__ == "__main__":
#     li = [7, 5, 4, 3, 2, 1]
#     quick_sort(li, 0, len(li)-1)
#     print(li)
