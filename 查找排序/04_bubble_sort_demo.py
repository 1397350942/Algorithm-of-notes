def bubble_sort(data_list):
    for i in range(len(data_list)):
        flug = False
        for j in range(len(data_list)-1-i):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                flug = True
        
    print(data_list)


if __name__ == "__main__":
    li = [i for i in range(1,20)]
    data_list = [1, 20, 6, 19, 21]
    bubble_sort(li)

# # [4,2,1,5]
# def bubble_sort(data_list):
#     """冒泡排序"""
#     for i in range(len(data_list)):
#         flug = False
#         for j in range(len(data_list)-1-i):
#             if data_list[j] > data_list[j+1]:
#                 data_list[j+1], data_list[j] = data_list[j], data_list[j+1]
#                 flug = True
#         print(data_list)
#         if flug == False:
#             return

# def bubble_sort(data_list):
#     for i in range(len(data_list)):
#         flug = False
#         for j in range(len(data_list)-i-1):
#             if data_list[j] > data_list[j+1]:
#                 data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
#                 flug = True

#         if flug == False:
#             print(data_list)
#             return
#         else:
#             print(data_list)
