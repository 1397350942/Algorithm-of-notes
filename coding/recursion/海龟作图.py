# 海龟作图

import turtle

t = turtle.Turtle()
win = turtle.Screen()


def draw(t, line_len):
    if line_len > 0:
        # 从左向右绘制
        t.forward(line_len)
        t.right(90)
        draw(t, line_len-5)


draw(t, 150)
