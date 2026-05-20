class myQueue:
    
    def __init__(self):
        # Initialize your data members
        self.s1 = [] # Input stack
        self.s2 = [] # Output stack

    def enqueue(self, x):
        # Enqueue operation: Hamesha s1 mein push karo
        self.s1.append(x)

    def dequeue(self):
        # Dequeue operation: Front element remove karna hai
        if self.size() == 0:
            return -1
            
        # Agar s2 khali hai, toh s1 ke saare elements s2 mein transfer karo
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        # S2 ke top se element remove karke return kar do
        return self.s2.pop()

    def front(self):
        # Return the front element of the queue
        if self.size() == 0:
            return -1
            
        # Agar s2 khali hai, toh s1 ke saare elements s2 mein transfer karo
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        # S2 ka top element hi queue ka front element hai
        return self.s2[-1]

    def size(self):
        # Return the current size of the queue
        # Total size dono stacks ke elements ka sum hoga
        return len(self.s1) + len(self.s2)