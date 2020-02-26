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

    def __remove_node_1(self, node):
        """情况1 node是叶子节点"""
        if not node.parent:  # 根节点
            self.root = None
        if node == node.parent.lchild:
            """node是它父亲的左孩子"""
            node.parent.lchild = None
        else:  # node是它的父亲的右孩子
            node.parent.rchild = None

    def __remove_node_2_1(self, node):
        """情况2.1: node只有一个左孩子"""
        if not node.parent:
            """如果是根节点"""
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_2_2(self, node):
        """情况2.2: node只有一个右孩子"""
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:  # 不存在
                return False
            if not node.lchild and not node.rchild:  # 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 2.1 只有一个左孩子
                self.__remove_node_2_1(node)
            elif not node.lchild:  # 情况 2.2 只有一个右孩子
                self.__remove_node_2_2(node)
            else:
                # 情况3
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_2_2(min_node)
                else:
                    self.__remove_node_2_1(min_node)


if __name__ == "__main__":
    tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    tree.pre_order(tree.root)
    print("")
    tree.in_order(tree.root)
    print("")
    tree.post_order(tree.root)
    
    tree.delete(4)
    tree.post_order(tree.root)