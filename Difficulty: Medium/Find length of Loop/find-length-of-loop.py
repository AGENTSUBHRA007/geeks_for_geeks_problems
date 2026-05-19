''' Structure for link list Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        
        if head is None or head.next is None:
            return 0
            
        fast = head
        slow = head
        
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next  # 2 steps
            slow = slow.next       # 1 step
            
            
            if fast == slow:
                
                count = 1
                curr = slow.next 
                
                
                while curr != slow:
                    count += 1
                    curr = curr.next
                    
                return count
                
        
        return 0