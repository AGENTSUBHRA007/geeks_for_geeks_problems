class Solution:
    def maxValue(self, arr): 
        
        arr.sort()
        
        total_sum = 0
        MOD = 10**9 + 7
        
        
        for i in range(len(arr)):
            total_sum += arr[i] * i
            
       
        return total_sum % MOD