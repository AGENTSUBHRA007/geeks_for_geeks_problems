'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        # Step 1: Naya node taiyar kiya
        new_node = Node(x) # Pythonically variable ka naam change kiya readable banane ke liye
        
        # Case 1: Agar list pehle se khali hai, toh naya node hi head banega
        if head is None:
            return new_node
            
        # Case 2: Agar list khali nahi hai, toh aakhri tak traverse karein
        curr = head
        while curr.next is not None: # FIX: Jab tak hum absolute last node par na pahunch jayein
            curr = curr.next
            
        # Aakhri node par pahunch kar naye node ko link kar diya
        curr.next = new_node
        
        # Original head ko hi return karenge taaki puri list barkarar rahe
        return head