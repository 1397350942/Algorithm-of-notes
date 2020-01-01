# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/1
"""


class Node(object):
    """节点类"""

    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = Node(0, None)
        self.tail = None

    def print(self):
        """遍历链表的值"""
        p = self.head
        if p == None:
            print("链表为空")
        print("总节点数:", self.head.value, end=" ")
        while p.next != None:
            p = p.next
            print(p.value, end=" ")
        print("\n")

    def add_first(self, value):
        """添加首节点"""
        next = self.head.next
        node = Node(value, next)
        self.head.next = node
        self.head.value += 1
        if self.head.value == 1:
            self.tail = node

    def add_tail(self, value):
        """添加尾节点"""
        if self.tail == None:
            self.add_first(value)
        else:
            node = Node(value, None)
            self.tail.next = node
            self.tail = node
            self.head.value += 1

    def insert_node(self, n, value):
        """插入任意位置"""
        if self.head == None:
            return
        if n < 1 or n > self.head.value:
            print("插入位置错误")
            return
        p = self.head
        i = 0
        while i < n:
            p = p.next
            i += 1
        node = Node(value, p.next)
        p.next = node
        if self.head.value == n:
            self.tail = node
        self.head.value += 1

    def remove_first(self):
        """移除第1个节点"""
        if self.head.next == None:
            print("链表没有节点,无法移除第1个节点")
            return
        p = self.head.next
        self.head.next = p.next
        self.head.value -= 1
        if self.head.value == 0:
            self.tail = None
        return p

    def remove_tail(self):
        """移除尾节点"""
        if self.head.next == None:
            print("链表没有节点,无法移除尾节点")
            return
        p = self.head
        while p.next != None:
            p1 = p  # 指向倒数第2个节点
            p = p.next
        p1.next = p.next
        self.head.value -= 1
        if self.head.value == 0:
            self.tail = None
            self.head.next = None
        else:
            self.tail = p1
        return p

    def remove_node(self, n):
        """移除任意位置节点"""
        if n < 1 or n > self.head.value:
            print("该节点不存在,无法移除")
            return
        p = self.head
        i = 0
        while i < n - 1:
            p = p.next
            i += 1
        p1 = p.next  # p1： 要移除的节点
        p.next = p1.next
        self.head.value -= 1
        if self.head.value == 0:
            self.tail = None
        elif p.next == None:
            self.tail = p
        return p1

    def search_node(self, value):
        """搜索节点"""
        if self.head == None:
            return
        p = self.head.next
        while p != None and p.value != value:
            p = p.next
        if p == None:
            print("没有找到值为{value}的节点".format(value=value))
            return
        return p

    def search_remove_node(self, value):
        """搜索并删除节点"""
        if self.head == None:
            return
        p = self.head.next
        p1 = self.head
        while p != None and p.value != value:
            p1 = p  # p1是待删除节点前一个节点
            p = p.next
        if p == None:
            print("没有找到值为{value}的节点".format(value=value))
            return
        p1.next = p.next
        self.head.value -= 1
        if self.head.value == 0:
            self.tail = None
        elif p1.next == None:
            self.tail = p1
        return p


if __name__ == '__main__':
    linked_list = LinkedList()
    print("------add_first\n")
    for value in [10, 20, 40, 60, 70]:
        linked_list.add_first(value)
    linked_list.print()
    print("链表尾部:{}".format(linked_list.tail.value))
    print("------insert_tail\n")
    linked_list.add_tail(5)
    linked_list.print()
    print("------insert_node\n")
    linked_list.insert_node(3, 30)
    linked_list.print()
    print("-----remove_first\n")
    linked_list.remove_first()
    linked_list.print()
    linked_list.remove_first()
    linked_list.print()
    print("-----remove_tail\n")
    linked_list.remove_tail()
    linked_list.print()
    print("-----remove_node\n")
    linked_list.remove_node(1)
    linked_list.print()
    print("-----search_node\n")
    value = 30
    node = linked_list.search_node(value)
    if node != None:
        print("{}节点已经找到".format(node.value))
    print("-------search_remove_node")
    linked_list.search_remove_node(value)
    linked_list.print()
