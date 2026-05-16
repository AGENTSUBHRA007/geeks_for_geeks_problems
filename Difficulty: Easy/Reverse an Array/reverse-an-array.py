class Solution:
    def reverseArray(self, arr):
        # 1. Put a pointer at the very start (0) and very end (len-1)
        left = 0
        right = len(arr) - 1
        
        # 2. Keep swapping until the pointers meet in the middle
        while left < right:
            
            # Swap the two numbers
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            
            # 3. Move the hands inward
            left += 1
            right -= 1
            
        return arr