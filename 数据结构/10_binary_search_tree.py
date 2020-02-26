class BiTreeNode(object):
    """二叉树搜索的节点类"""

    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST(object):
    """二叉搜索树"""

    def __init__(self, li):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        """插入值 递归写法"""
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:    # 空树的情况
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 如果左孩子已经存在
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:  # 什么也不做
                return

    def pre_order(self, root):
        """前序遍历"""
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        """中序遍历"""
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self, root):
        """后序遍历"""
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    def query(self, node, val):
        """查询 递归版本"""
        if not node:  # 空树 直接返回None
            return None
        elif node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None


if __name__ == "__main__":
    tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    tree.pre_order(tree.root)
    print("")
    tree.in_order(tree.root)
    print("")
    tree.post_order(tree.root)
    print(tree.query_no_rec(4))
