# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None

class Solution:
    def fractionalNode(self, head, k):
        
        if head is None:
            return None
            
        
        count = 0
        curr = head
        while curr is not None: 
            count += 1
            curr = curr.next
            
        
        
        pos = (count + k - 1) // k
        
        
        curr = head
        
        for i in range(pos - 1):
            curr = curr.next
            
        
        return curr.data