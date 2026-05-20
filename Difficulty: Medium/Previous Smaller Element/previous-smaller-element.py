class Solution:
    # FIX: function ka naam badal kar 'leftSmaller' kiya
    def prevSmaller(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            current = arr[i]
            
            while stack and stack[-1] >= current:
                stack.pop()
                
            if stack:
                result[i] = stack[-1]
                
            stack.append(current)
            
        return result