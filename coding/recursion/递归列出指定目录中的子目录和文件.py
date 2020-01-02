# -*- coding:utf-8  -*-
"""
author: wengwenyu@aliyun.com 
date: 2020/1/2
"""
# 递归列出指定目录中的子目录和文件
# C:\Users\wengw\Documents\Algorithm-of-notes\coding
import os


def disk_recursion(path):
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            disk_recursion(child_path)
        print(path)


disk_recursion("C:\\Users\\wengw\\Documents\\Algorithm-of-notes\\coding")
