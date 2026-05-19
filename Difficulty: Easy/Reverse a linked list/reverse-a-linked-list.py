"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            # 1. Agli node ko safe side save kar lo taaki link tootne par list na kho jaye
            next_node = curr.next
            
            # 2. Current node ka pointer piche (prev) ki taraf ghuma do
            curr.next = prev
            
            # 3. prev aur curr dono pointers ko ek-ek step aage khiskao
            prev = curr
            curr = next_node
            
        # Jab loop khatam hoga, curr None ho jayega aur prev naye head par baitha hoga
        return prev