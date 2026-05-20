class TwoStacks:
    def __init__(self):
        # Ek fixed size array banaya (e.g., 200 size ka)
        self.size = 200
        self.arr = [0] * self.size
        
        # Stack 1 shuru hoga index 0 ke peeche se (-1)
        self.top1 = -1
        # Stack 2 shuru hoga aakhri index ke aage se (self.size)
        self.top2 = self.size

    # Function to push an integer into stack 1
    def push1(self, x):
        # Check karo ki kya dono stacks ke beech mein jagah bachi hai?
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x

    # Function to push an integer into stack 2
    def push2(self, x):
        # Check karo ki kya dono stacks ke beech mein jagah bachi hai?
        if self.top1 + 1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x

    # Function to remove an element from top of stack 1
    def pop1(self):
        # Agar top1 abhi bhi -1 par hai, matlab stack 1 khali hai
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        # Agar top2 abhi bhi size par hai, matlab stack 2 khali hai
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        return -1