def select_sort_simple(data_list):
    """选择排序"""
    data_list_new = []
    for i in range(len(data_list)):
        min_value = min(data_list)
        data_list_new.append(min_value)
        data_list.remove(min_value)
    return data_list_new


def select_sort(data_list):
    """选择排序O(n^2)"""
    for i in range(len(data_list)-1):
        min_local = i
        for j in range(i, len(data_list)):
            if data_list[j] < data_list[min_local]:
                min_local = j
        data_list[min_local], data_list[i] = data_list[i], data_list[min_local]
    return data_list


if __name__ == "__main__":
    li = [9, 6, 4, 1, 2]
    print(select_sort(li))

# def select_sort(data_list):
#     """选择排序"""
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[i], data_list[min_local] = data_list[min_local], data_list[i]
#     return data_list

# def select_sort(data_list):
#     """选择排序"""
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[i], data_list[min_local] = data_list[min_local], data_list[i]
#     return data_list

# def select_sort(data_list):
#     """选择排序"""
#     # [1,3,2,5,6]
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[min_local], data_list[i] = data_list[i], data_list[min_local]
#     return data_list

# def select_sort(data_list):
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i,len(data_list)):
#             if data_list[min_local] > data_list[j]:
#                 min_local = j
#         data_list[i],data_list[min_local] = data_list[min_local],data_list[i]
#     return data_list

# def select_sort(data_list):
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[i], data_list[min_local] = data_list[min_local], data_list[i]

# def select_sort(data_list):
#     """选择排序"""
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i+1, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[i], data_list[min_local] = data_list[min_local], data_list[i]
#     return data_list

# def select_sort(data_list):
#     """选择排序"""
#     for i in range(len(data_list)-1):
#         min_local = i
#         for j in range(i+1, len(data_list)):
#             if data_list[j] < data_list[min_local]:
#                 min_local = j
#         data_list[min_local], data_list[i] = data_list[i], data_list[min_local]
#     return data_list
