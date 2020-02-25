# class LinkList(object):
#     class Node(object):
#         """节点类"""

#         def __init__(self, item=None):
#             self.item = item
#             self.next = None

#     class LinkListIterator(object):
#         def __init__(self, node):
#             self.node = node

#         def __next__(self):
#             if self.node:
#                 cur_node = self.node
#                 self.node = cur_node.next
#                 return cur_node.item
#             else:
#                 raise StopIteration

#         def __iter__(self):
#             return self

#     def __init__(self, iterble=None):
#         self.head = None
#         self.tail = None
#         if iterble:
#             self.extend(iterble)

#     def append(self, obj):
#         s = LinkList.Node(obj)
#         if not self.head:
#             self.head = s
#             self.tail = s
#         else:
#             self.tail.next = s
#             self.tail = s

#     def extend(self, iterable):
#         for obj in iterable:
#             self.append(obj)

#     def find(self, obj):
#         for n in self:
#             if n == obj:
#                 return True
#         else:
#             return False

#     def __iter__(self):
#         return self.LinkListIterator(self.head)

#     def __repr__(self):
#         return "<<"+",".join(map(str, self))+">>"


# if __name__ == "__main__":
#     lk = LinkList([1, 2, 3, 4, 5])
#     for element in lk:
#         print(element)
#     print(lk)  # 重写repr

# class LinkList(object):
#     class Node(object):
#         """链表的节点类"""

#         def __init__(self, item=None):
#             self.item = item
#             self.next = None

#     class LinkListIterator(object):
#         def __init__(self, node):
#             self.node = node

#         def __next__(self):
#             if self.node:
#                 cur_node = self.node
#                 self.node = cur_node.next
#                 return cur_node.item
#             else:
#                 raise StopIteration

#         def __iter__(self):
#             return self

#     def __init__(self, iterble=None):
#         self.head = None
#         self.tail = None
#         if iterble:
#             self.extend(iterble)

#     def append(self, obj):
#         """单个元素 尾插法添加"""
#         s = LinkList.Node(obj)
#         if not self.head:
#             self.head = s
#             self.tail = s
#         else:
#             self.tail.next = s
#             self.tail = s

#     def extend(self, iterble):
#         """多个元素"""
#         for obj in iterble:
#             self.append(obj)

#     def find(self, obj):
#         """查找元素"""
#         for n in self:
#             if n == obj:
#                 return True
#         else:
#             return False

#     def __iter__(self):
#         return self.LinkListIterator(self.head)

#     def __repr__(self):
#         return "<<"+",".join(map(str, self))+">>"


# if __name__ == "__main__":
#     lk = LinkList([1, 2, 3, 4, 5])
#     for element in lk:
#         print(element)
#     print(lk)
#     print(lk.find(2))

class LinkList(object):
    class Node(object):
        """链表节点类"""

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

    def extend(self, iterble):
        for obj in iterble:
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


if __name__ == "__main__":
    lk = LinkList([1, 2, 3, 4, 5])
    for element in lk:
        print(element)
    print(lk)
