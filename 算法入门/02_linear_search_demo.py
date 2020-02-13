def linear_search(data_list, value):
    """顺序查找"""
    for i in range(len(data_list)):
        if data_list[i] == value:
            return i
    else:
        return None


if __name__ == "__main__":
    data_list = [1, 2, 3, 4, 5]
    print(linear_search(data_list, 1))
    pass

# def linear_search(data_list, value):
#     """顺序查找"""
#     for i, v in enumerate(data_list):
#         if v == value:
#             return i
#     else:
#         return None


# def linear_search(data_list, value):
#     for i in range(len(data_list)):
#         if data_list[i] == value:
#             return i
#     return None

# def linear_search(data_list, value):
#     """顺序查找"""
#     for i in range(len(data_list)):
#         if data_list[i] == value:
#             return i
#     else:
#         return None
