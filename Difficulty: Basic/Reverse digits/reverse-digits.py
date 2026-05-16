#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
	    d = n
        rev_num = 0  
        
        while d > 0:  
            
            
            rem = d % 10
            
            
            rev_num = (rev_num * 10) + rem
            
            
            d = d // 10
            
        return rev_num