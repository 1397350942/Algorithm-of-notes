def binary_search(data_list, value):
    """二分查找,折半查找"""
    left = 0
    right = len(data_list)
    while left <= right:
        mid = (right+left)//2
        if data_list[mid] == value:
            return mid
        elif data_list[mid] < value:
            left = mid + 1
        elif data_list[mid] > value:
            right = mid - 1
    return None


if __name__ == "__main__":
    li = [1, 2, 3, 4, 5, 6]
    print(binary_search(li, 5))
# def binary_search(data_list, value):
#     """二分查找,折半查找"""
#     left = 0
#     right = len(data_list)
#     while left <= right:
#         mid = (right+left)//2
#         if data_list[mid] == value:
#             return mid
#         elif data_list[mid] > value:
#             right = mid - 1
#         elif data_list[mid] < value:
#             left = mid + 1
#     return None


# def binary_search(data_list, value):
#     left = 0
#     right = len(data_list)
#     while left <= right:
#         mid = (left+right)//2
#         if data_list[mid] == value:
#             return mid
#         elif data_list[mid] > value:
#             right = mid - 1
#         elif data_list[mid] < value:
#             left = mid + 1
#     return None
