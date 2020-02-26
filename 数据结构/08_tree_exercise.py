class Node(object):

    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type  # "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree(object):
    """模拟文件系统"""

    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 以/ 结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        self.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        """相对路径"""
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


if __name__ == "__main__":
    tree = FileSystemTree()
    tree.mkdir("var/")
    tree.mkdir("usr/")
    tree.mkdir("bin/")

    tree.cd("bin/")
    tree.mkdir("python/")

    print(tree.ls())
