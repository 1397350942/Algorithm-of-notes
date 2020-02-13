import sys
n = 100

data = []  # 默认尺寸: 64 bytes
for i in range(n):
    a = len(data)  # 列表实际元素个数
    b = sys.getsizeof(data)  # 分配给列表的空间尺寸(单位: 字节)
    print("列表实际元素的个数{0:3d};\n列表占用的字节数{1:4d}".format(a, b))
    data.append(i)
