import ctypes


class DynamicArray(object):
    """实现动态数组"""

    def __init__(self):
        self.count = 0  # 数组中实际的元素
        self.capacity = 1  # 数组预分配的空间
        self.A = self.make_array(self.capacity)

    def make_array(self, c):
        return (c*ctypes.py_object)()

    def len(self):
        return self.count

    def getitems(self, k):
        if not 0 <= k < self.count:
            raise IndexError("invalid index")
        return self.A[k]

    def resize(self, c):
        B = self.make_array(c)
        for k in range(self.count):
            B[k] = self.A[k]
        self.A = B
        self.capacity = c

    def append(self, obj):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.A[self.count] = obj
        self.count += 1

    def insert(self, k, value):
        if self.count == self.capacity:
            self.resize(2*self.capacity)

        for i in range(self.count, k, -1):
            self.A[i] = self.A[i-1]
        self.A[k] = value
        self.count += 1

    def remove(self, value):
        for k in range(self.count):
            if self.A[k] == value:
                for i in range(k, self.count-1):
                    self.A[i] = self.A[i+1]
                self.A[self.count] = None
                self.count -= 1
                return
        raise ValueError("value not found")


"""
array_type = (4*ctypes.c_char_p)
names = array_type()
print(type(names))
print(len(names))
s = ctypes.c_char_p("hello".encode("utf-8"))
names[0] = s
print(names[0])
"""
if __name__ == "__main__":
    dynamic_array = DynamicArray()
    for i in range(0, 20):
        dynamic_array.append(i)
    print(dynamic_array.len())
    dynamic_array.insert(3, 123)
    dynamic_array.remove(123)
    print(dynamic_array.getitems(3))

