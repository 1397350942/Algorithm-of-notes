# 将整数转换为任意进制的字符串
"""
十进制数:11 如何转换为二进制 

11 % 2 = 1
11 // 2 = 5  5 % 2 = 1 
5 // 2 = 2   2 % 2 = 0 
2 // 2 = 1   1 % 2 = 1

结果: 1011

十进制数:11 如何转换为十六进制
十六进制:0 1 2 3 4 5 6 7 8 9  A B C D E F

11 % 16 = 11 B 
"""


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


if __name__ == "__main__":
    print(to_str(11, 2))
    print(to_str(11, 8))
    print(to_str(11, 16))
