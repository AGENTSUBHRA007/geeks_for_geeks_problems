#User function Template for python3
# arr1 number[] 
# arr2 number[] 
# return boolean
class Solution:
    def isIdentical(self, a, b):
        b.sort()
        a.sort()
        if a==b:
            return True
        return False