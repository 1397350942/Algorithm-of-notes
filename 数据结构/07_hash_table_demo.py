class LinkList(object):
    class Node(object):
        """节点类"""

        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator(object):
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterble=None):
        self.head = None
        self.tail = None
        if iterble:
            self.extend(iterble)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+",".join(map(str, self))+">>"


class HashTable(object):
    """类似集合 的 哈希表"""

    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def insert(self, k):
        i = self.h(k)  # 位置
        if self.find(k):
            print("Duplicated Insert")  # 重复的插入
        else:
            self.T[i].append(k)





if __name__ == "__main__":
    ht = HashTable()
    # ht.insert(0)
    # ht.insert(1)
    # ht.insert(0)
    ht.insert(0)
    ht.insert(1)
    ht.insert(3)
    ht.insert(102)
    print(",".join(map(str, ht.T)))
# class HashTable2(object):
#     """类似集合的哈希表"""

#     def __init__(self, size=101):
#         self.size = size
#         self.T = [LinkList() for _ in range(self.size)]

#     def h(self, k):
#         return k % self.size

#     def find(self, k):
#         i = self.h(k)
#         return self.T[i].find(k)

#     def insert(self, k):
#         i = self.h(k)  # 位置
#         if self.find(k):
#             print("Duplicated Insert")
#         else:
#             self.T[i].append(k)