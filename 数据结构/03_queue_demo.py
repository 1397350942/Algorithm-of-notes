class Queue(object):
    """环形队列"""

    def __init__(self, size=100):
        self.size = size
        self.queue = [0 for _ in range(size)]
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        """入队"""
        if self.is_filled():
            raise IndexError("Queue is filled")
        self.rear = (self.rear+1) % self.size
        self.queue[self.rear] = element

    def pop(self):
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front = (self.front+1) % self.size
        return self.queue[self.front]

    def is_empty(self):
        """判断队空"""
        return self.rear == self.front

    def is_filled(self):
        """判断队满"""
        return (self.rear+1) % self.size == self.front


if __name__ == "__main__":
    queue = Queue(5)
    for i in range(4):
        queue.push(i)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
