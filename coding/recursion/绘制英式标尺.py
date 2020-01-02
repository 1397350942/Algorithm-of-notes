# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""


# 用来绘制刻度线
def draw_line(tick_length, tick_label=""):
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


# 用来绘制英寸之间的刻度
def draw_interval(center_length):
    if center_length > 0:
        # 绘制中心线左半部分
        draw_interval(center_length - 1)
        # 绘制中心线
        draw_line(center_length)
        # 绘制中心线右半部分
        draw_interval(center_length - 1)


# 绘制标尺
def draw_ruler(num_inches, major_length):
    draw_line(major_length, "0")
    for k in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(k))


if __name__ == '__main__':
    draw_ruler(5, 8)
