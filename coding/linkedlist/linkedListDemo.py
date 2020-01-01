# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/1
"""
"""
1. 添加首节点 
2. 添加尾节点 
3. 在任意位置插入节点
4. 移除首节点 
5. 移除尾节点 
6. 移除任意节点
7. 搜索节点 
8. 搜索并移除节点 
"""


class Node(object):
    """节点类"""

    def __init__(self, value, next):
        self.value = value
        self.next = next


def print_linked_list(head):
    """输出链表"""
    p = head
    if p == None:
        print("链表为空")
    else:
        print(head.value, end=" ")
        while p.next != None:
            p = p.next
            print(p.value)


def add_first(head, value):
    """添加首节点"""
    next = head.next  # 得到第一个节点的地址
    node = Node(value, next)
    head.next = node  # 头结点重新指向新节点
    head.value += 1


def find_tail(head):
    """找到尾节点"""
    p = head
    while p.next != None:
        p = p.next
    return p


def add_tail(head, value):
    """添加尾节点"""
    tail_node = find_tail(head)  # 获得尾节点
    node = Node(value, None)
    tail_node.next = node
    head.value += 1


########## 改进版的 add_tail ##########
def add_first_ext(head, value):
    next = head.next
    node = Node(value, next)
    if next is None:
        head.tail = node
    head.next = node
    head.value += 1


def add_tail_ext(head, value):
    node = Node(value, None)
    tail = head.tail
    if tail == None:
        tail = head
    tail.next = node
    head.tail = node
    head.value += 1


def insert_node(head, n, value):
    """将一个新的节点插入到链表任意位置"""
    if head is None:
        return
    if n < 1 or n > head.value:
        """位置判断,如果小于1或者比链表还长"""
        print("插入位置错误")
        return
    p = head
    i = 0
    while i < n:
        p = p.next
        i += 1
    node = Node(value, p.next)
    p.next = node
    head.value += 1


def remove_first(head):
    """移除首节点"""
    if head == None:
        return
    if head.next == None:
        return
    p = head.next
    head.next = p.next  # 将第2个节点赋给头节点的next
    head.value -= 1


def remove_tail(head):
    """移除尾节点"""
    if head == None:
        return
    p = head
    # 找到尾节点
    while p.next != None:
        p1 = p  # 倒数第2个节点
        p = p.next

    p1.next = p.next
    head.value -= 1
    return p.value


def remove_node(head, n):
    """移除任意的节点"""
    if head == None:
        return
    if n < 1 or n > head.value:
        print("该节点不存在,无法删除")
        return
    p = head
    i = 0
    while i < n - 1:
        p = p.next
        i += 1
    p1 = p.next  # p1是待删除的节点
    p.next = p1.next
    head.value -= 1
    return p


def search_node(head, value):
    """搜索节点"""
    if head == None:
        return
    p = head.next
    while p != None and p.value != value:
        p = p.next
    if p == None:
        print("没有找到值为{value}的节点".format(value=value))
        return
    return p


def search_remove_node(head, value):
    """搜索并删除节点"""
    if head == None:
        return
    p = head.next
    p1 = head
    while p != None and p.value != value:
        p1 = p  # p1 是待删除节点前一个节点
        p = p.next
    if p == None:
        print("没有找到值为{value}的节点".format(value=value))
    head.value -= 1
    return p


if __name__ == '__main__':
    ######### add_first#############
    head = Node(0, None)
    for value in [60, 50, 40, 30, 20]:
        add_first(head, value)
    # print_linked_list(head)
    add_first(head, 10)
    # print_linked_list(head)
    ######### add_tail#############
    add_tail(head, 70)
    # print_linked_list(head)
    ######### add_tail_ext ###########
    new_head = Node(0, None)
    for value in [60, 50, 40, 30, 20, 10]:
        add_first_ext(new_head, value)
    add_tail_ext(new_head, 70)
    # print_linked_list(new_head)
    ######## insert_node ###########
    insert_node(new_head, 1, 15)
    print_linked_list(new_head)
    print("######## remove_first###########")
    remove_first(head)
    print_linked_list(head)
    print("##########移除尾节点#################")
    print(remove_tail(head))
    print(remove_tail(head))
    # print_linked_list(head)
    print("###########search_node###########")
    node = search_node(new_head, 50)
    print(node.value)
    print_linked_list(head)
    print("搜索并删除节点")
    search_remove_node(head,50)
    print_linked_list(head)
