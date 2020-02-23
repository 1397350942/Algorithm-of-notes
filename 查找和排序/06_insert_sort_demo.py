def insert_sort(data_list):
    """插入排序"""
    for i in range(1, len(data_list)):
        tmp = data_list[i]
        j = i - 1
        while j >= 0 and data_list[j] > tmp:
            data_list[j+1] = data_list[j]
            j = j - 1
        data_list[j+1] = tmp
    return data_list


if __name__ == "__main__":
    print(insert_sort([3, 4, 5, 1, 2]))

# def insert_sort(data_list):
#     """插入排序"""
#     for i in range(1, len(data_list)):
#         tmp = data_list[i]
#         j = i - 1
#         while j >= 0 and data_list[j] > tmp:
#             data_list[j+1] = data_list[j]
#             j = j - 1
#         data_list[j+1] = tmp
#     return data_list

# if __name__ == "__main__":
#     print(insert_sort([4,5,1,2,3]))


# def insert_sort(data_list):
#     for i in range(1, len(data_list)):
#         tmp = data_list[i]
#         j = i - 1
#         while j >= 0 and tmp < data_list[j]:
#             data_list[j+1] = data_list[j]
#             j = j - 1
#         data_list[j+1] = tmp
#     return data_list


# if __name__ == "__main__":
#     print(insert_sort([5, 4, 2, 9, 1]))


# def insert_sort(data_list):
#     for i in range(1, len(data_list)):
#         tmp = data_list[i]
#         j = i - 1
#         while j >= 0 and tmp < data_list[j]:
#             data_list[j+1] = data_list[j]
#             j = j - 1
#         data_list[j+1] = tmp
#     return data_list

# if __name__ == "__main__":
#     print(insert_sort([5,4,2,9,1]))


# def insert_sort(data_list):
#     for i in range(1,len(data_list)):
#         tmp = data_list[i]
#         j = i-1
#         while j >= 0 and data_list[j] > tmp:
#             data_list[j+1] = data_list[j]
#             j -= 1
#         data_list[j+1] = tmp
#         print(data_list)

# if __name__ == "__main__":
#     data_list = [3,2,5,7,8]
#     print(data_list)
#     insert_sort(data_list)
