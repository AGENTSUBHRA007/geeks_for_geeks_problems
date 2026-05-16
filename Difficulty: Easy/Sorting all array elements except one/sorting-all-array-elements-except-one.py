class Solution:

    def sort_except_k(self, arr, k):
        # code here
        saved=arr[k]
        arr.pop(k)
        arr.sort()
        arr.insert(k,saved)
        return arr

        
