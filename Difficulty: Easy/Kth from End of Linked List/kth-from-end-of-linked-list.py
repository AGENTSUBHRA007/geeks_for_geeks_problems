''' Structure of linked list Node
	{
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        first=head
        second=head
        for i in range (k):
            if first is None:
                return -1
            else:
                first=first.next
        
        while first is not None:
            first=first.next
            second=second.next
        
        return second.data
            
            
        