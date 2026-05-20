class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.stack = []
        self.n = n

    def isEmpty(self):
        # Check if stack is empty (Returns True or False)
        return len(self.stack) == 0

    def isFull(self):
        # Check if stack is full (Returns True or False)
        return len(self.stack) == self.n

    def push(self, x):
        # Insert x at the top of the stack if it's not full
        if self.isFull():
            return
        self.stack.append(x)

    def pop(self):
        # Removes an element from the top of the stack if not empty
        if self.isEmpty():
            return
        return self.stack.pop()

    def peek(self):
        # Returns the top element of the stack if not empty, else -1
        if self.isEmpty():
            return -1
        return self.stack[-1]