# 海龟作图 用递归法绘制一棵树
import turtle


def tree(branch_len, t):
    if branch_len > 5:
        # 绘制树干
        t.forward(branch_len)
        # 向右侧旋转20度
        t.right(20)
        # 绘制右侧的分支
        tree(branch_len - 15, t)
        # 向左侧旋转40度
        t.left(40)
        # 绘制左侧的分支
        tree(branch_len-15, t)
        # 将绘制的方向归为(从下到上)
        t.right(20)
        t.backward(branch_len)


if __name__ == "__main__":

    t = turtle.Turtle()
    win = turtle.Screen()
    # 逆时针旋转90度,绘制方向变成了从下到上
    t.left(90)
    # 画笔颜色
    t.pencolor("green")

    tree(70, t)
    win.exitonclick()
