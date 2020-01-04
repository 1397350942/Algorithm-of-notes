"""
[1,2,4,6,7,10,12,56]
"""


def list_num(num_list):
    """非递归方式"""
    result = 0
    for i in num_list:
        result += i
    return result


def list_num_recursion(num_list):
    """递归"""
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_num_recursion(num_list[1:])


if __name__ == "__main__":
    l = [1, 2, 4, 6, 7, 10, 12, 56]
    print(list_num(l))
