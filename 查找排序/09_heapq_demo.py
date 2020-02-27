import heapq  # 堆的内置模块
import random

dataset = list(range(10))
random.shuffle(dataset)
print(dataset)
heapq.heapify(dataset)  # 建堆
# heapq.heappop(dataset) # 每次都会弹出一个最小的元素
for i in range(len(dataset)):
    print(heapq.heappop(dataset), end=" ")
