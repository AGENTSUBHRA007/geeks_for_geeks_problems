class Solution:
    def findMagicalNumber(self, arr):
        for i in range(len(arr)):
            if arr[i] == i:
                return i
         
        return -1  