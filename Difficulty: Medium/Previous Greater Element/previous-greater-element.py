class Solution:
    def preGreaterEle(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []
        
        
        for i in range(n):
            current = arr[i]
            
            
            while stack and stack[-1] <= current:
                stack.pop()
                
            
            if stack:
                result[i] = stack[-1]
                
            
            stack.append(current)
            
        return result