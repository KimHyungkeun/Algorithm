# 시간 초과
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums :
            return nums
        
        result = []
        q = deque(nums[:k])
        max_val = max(q)
        result.append(max_val)
        
        
        for i in range(k, len(nums)) :
            
            q.append(nums[i])
            q.popleft()
            
            if max_val < nums[i] :
                max_val = nums[i]
            
            else :
                if max_val not in q :
                    max_val = max(q)
                    
       
            result.append(max_val)
            # print(q)
            
        return result