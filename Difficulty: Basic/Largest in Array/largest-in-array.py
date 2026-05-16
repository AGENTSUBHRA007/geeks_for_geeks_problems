class Solution:
    def largest(self, arr):
        # code here
        biggest=arr[0]
        for num in arr:
            if num> biggest:
                biggest=num
        return biggest
                
        
