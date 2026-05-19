''' Structure for link list Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def sortedMerge(self, head1, head2):
        
        new = Node(-1)
        head = new
        
        curr1 = head1
        curr2 = head2
        
        
        while curr1 is not None and curr2 is not None:
            
            if curr1.data < curr2.data:
                head.next = curr1      
                curr1 = curr1.next    
            else:
                head.next = curr2      
                curr2 = curr2.next    
                
            head = head.next           
            
        
        
        if curr1 is not None:
            head.next = curr1
        else:
            head.next = curr2
            
        
        return new.next