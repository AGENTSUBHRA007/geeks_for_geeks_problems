class Solution:
    def palindromicSubstr(self, s):
        # code here
  
        distinct_palindromes = set()
        n = len(s)
        
        for i in range(n):
            
            # --- 1. Find Odd-Length Palindromes ---
            # Center is exactly at index 'i'
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                distinct_palindromes.add(s[left : right + 1])
                left -= 1   # Expand left
                right += 1  # Expand right
                
            # --- 2. Find Even-Length Palindromes ---
            # Center is between index 'i' and 'i+1'
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                distinct_palindromes.add(s[left : right + 1])
                left -= 1   # Expand left
                right += 1  # Expand right
                
        # The problem allows returning in any order, so we just convert the set to a list
        return list(distinct_palindromes)