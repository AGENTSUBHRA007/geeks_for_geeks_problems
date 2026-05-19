class Solution:
    def deleteMid(self, head):
        # Edge Case: Agar list khali hai ya sirf ek node hai
        if head is None or head.next is None:
            return None
            
        slow = head
        fast = head
        prev = None # Slow node se thik ek kadam piche chalne ke liye
        
        # Fast pointer 2 kadam chalega aur slow pointer 1 kadam
        while fast is not None and fast.next is not None:
            fast = fast.next.next  # 2 steps
            prev = slow            # Slow ka pichla node track kiya
            slow = slow.next       # 1 step
            
        # Jab loop rukega, 'slow' exact middle node par hoga 
        # aur 'prev' usse thik ek node pehle hoga.
        prev.next = slow.next # Middle node ka connection kaat diya!
        
        return head