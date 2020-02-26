from collections import deque


class BiTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


def pre_order(root):
    """前序遍历"""
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    """中序遍历"""
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


def post_order(root):
    """后序遍历"""
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


def level_order(root):
    """层次遍历"""
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


if __name__ == "__main__":
    a = BiTreeNode("A")
    b = BiTreeNode("B")
    c = BiTreeNode("C")
    d = BiTreeNode("D")
    e = BiTreeNode("E")
    f = BiTreeNode("F")
    g = BiTreeNode("G")

    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f

    root = e
    # print(root.lchild.rchild.data)
    # pre_order(root)
    # in_order(root)
    # post_order(root)
    level_order(root)
