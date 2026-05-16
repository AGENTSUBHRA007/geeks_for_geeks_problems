class Solution:
    def canFormPalindrome(self, s):
       
        unpaired_chars = set()
        
       
        for i in range(len(s)):
            char = s[i]
          
            if char in unpaired_chars:
                unpaired_chars.remove(char)
           
            else:
                unpaired_chars.add(char)
                
       
        if len(unpaired_chars) <= 1:
            return True
        else:
            return False