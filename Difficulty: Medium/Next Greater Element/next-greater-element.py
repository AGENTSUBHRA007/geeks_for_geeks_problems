class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        # Shuruat mein saare answers ko -1 se fill kar dete hain
        result = [-1] * n
        stack = []
        
        # Array ko piche se (Right to Left) scan karenge
        for i in range(n - 1, -1, -1):
            current = arr[i]
            
            # Jab tak stack khali nahi hai aur top element chhota ya barabar hai, use pop karo
            while stack and stack[-1] <= current:
                stack.pop()
                
            # Agar stack mein kuch bacha hai, toh wahi next greater element hai
            if stack:
                result[i] = stack[-1]
                
            # Current element ko stack mein push karo taaki yeh piche waalon ke liye option bane
            stack.append(current)
            
        return result