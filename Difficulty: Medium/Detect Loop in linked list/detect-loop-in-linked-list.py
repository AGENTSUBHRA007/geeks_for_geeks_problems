class Solution:
    def detectLoop(self, head):
        if head is None or head.next is None:
            return False
            
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next        # 1 step khisla
            fast = fast.next.next   # 2 steps khiska
            
            # Agar fast aur slow pointer aapas mein mil gaye, toh loop hai!
            if slow == fast:
                return True
                
        # Agar fast pointer None par pahunch gaya, toh koi loop nahi hai
        return False