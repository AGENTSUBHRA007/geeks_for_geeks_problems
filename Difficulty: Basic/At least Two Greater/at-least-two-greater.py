class Solution:
    def findElements(self, arr):
        # 1. Indentation: These lines must be pushed in to belong to the function
        arr.sort()
        k = len(arr)
        
        # 2. Slicing: Python uses square brackets [] for lists, not parentheses ()
        return arr[0 : k-2 : 1]