class Stack(object):
    """栈"""

    def __init__(self):
        self.stack = []

    def push(self, element):
        """入栈"""
        self.stack.append(element)

    def pop(self):
        """出栈"""
        if len(self.stack) < 0:
            return None
        return self.stack.pop()

    def get_top(self):
        """获取栈顶"""
        if len(self.stack) < 0:
            return None
        return self.stack[-1]


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
