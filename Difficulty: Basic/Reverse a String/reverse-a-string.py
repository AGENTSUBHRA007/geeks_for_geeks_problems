#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        reverse_string=""
        for i in range(len(s)-1,-1,-1):
            reverse_string+=s[i]
        return reverse_string