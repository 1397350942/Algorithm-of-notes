class Stack(object):
    """栈"""

    def __init__(self):
        self.stack = []

    def push(self, element):
        """入栈"""
        self.stack.append(element)

    def pop(self):
        """出栈"""
        if self.is_empty():
            return None
        return self.stack.pop()

    def get_top(self):
        """获取栈顶"""
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


"""
栈的应用: 括号匹配问题
([{}])  匹配
[{()}]  匹配
()(  不匹配
[{]} 不匹配
"""


def brace_match(s):
    """匹配括号"""
    match = {"}": "{", "]": "[", ")": "("}
    stack = Stack()
    for ch in s:
        if ch in ["(", "[", "{"]:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:  # stack.get_top() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print("==========括号匹配=========")
    print(brace_match("[({})(){}]"))
    print(brace_match("[]("))
