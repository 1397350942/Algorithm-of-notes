"""迷宫问题"""
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y:(x+1, y),
    lambda x, y:(x-1, y),
    lambda x, y:(x, y+1),
    lambda x, y:(x, y-1)
]


def maze_path(x1, y1, x2, y2):
    """使用栈的方式解决迷宫问题"""
    stack = []
    stack.append((x1, y1))  # 起始节点(坐标)
    while len(stack) > 0:
        curNode = stack[-1]  # 当前节点(坐标)
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点 输出路径
            for p in stack:
                print(p)
            return True
        # 假设当前坐标是x,y
        # 上 x-1,y 下 x+1,y 左 x,y-1 右 x,y+1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走,入栈并标记为2 2表示已经走过
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:  # 一个节点都找不到 就回退
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False


if __name__ == "__main__":
    maze_path(1, 1, 8, 8)
