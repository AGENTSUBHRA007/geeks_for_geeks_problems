'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        # Step 1: Naya node taiyar kiya
        new_node = Node(val)
        
        # EDGE CASE 1: Agar position 1 hai, toh naya node hi head banega
        if pos == 1:
            new_node.next = head
            return new_node # Ab naya node naya head ban gaya hai
            
        curr = head
        
        # Step 2: Sahi position tak pahunchne ke liye loop chalayein
        for i in range(pos - 2): # pos - 2 tak chalayenge taaki hum insertion point se thik ek node pehle rukein
            if curr is None or curr.next is None:
                # Agar position list ki length se bahar hai, toh insertion possible nahi hai
                return head # Ya fir question ke mutabik jo bhi unka invalid return type ho
            curr = curr.next
            
        # EDGE CASE 2: Agar loop ke baad bhi curr None hai (safari check)
        if curr is None:
            return head
            
        # Step 3: Pointers ko re-link karne ka aapka mast logic (With clean variables)
        remaining_list = curr.next
        curr.next = new_node
        new_node.next = remaining_list
        
        return head