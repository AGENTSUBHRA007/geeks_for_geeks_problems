''' Structure for link list Node
    class Node:
        def __init__(self, val):
            self.data = val
            self.next = None
'''

class Solution:
    def sumofNodes(self, head, n):
        
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
            
        
        total_sum = 0
        curr = head 
        
        
        if n >= count:
            while curr is not None:
                total_sum += curr.data
                curr = curr.next
                
        
        else:
            
            for i in range(count - n):
                curr = curr.next
                
            
            while curr is not None:
                total_sum += curr.data
                curr = curr.next
                
        return total_sum