class Solution:
    def find(self, arr: list, x: int) -> list:
        
        def bound(is_left: bool) -> int:
            start = 0
            end = len(arr) - 1
            Bound = -1
            
           
            while start <= end:
                mid = (start + end) // 2
                
                if arr[mid] == x:
                    Bound = mid
                   
                    if is_left:
                        end = mid - 1  
                    else:
                        start = mid + 1
                        
              
                elif arr[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1
                    
         
            return Bound
            
        first_pos = bound(is_left=True)
        last_pos = bound(is_left=False)
        
        return [first_pos, last_pos]