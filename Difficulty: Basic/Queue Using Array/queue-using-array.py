class myQueue:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, x):
        if self.isFull():
            return  # Queue is full, cannot enqueue
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            return  # Queue is empty, cannot dequeue
        if self.front == self.rear:
            # Only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]