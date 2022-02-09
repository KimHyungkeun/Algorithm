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

# p.574 풀이인데 이것도 시간초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        cur_max = float('-inf')
        for i, v in enumerate(nums) :
            window.append(v)
            if i < k - 1 :
                continue
            
            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if cur_max == float('-inf') :
                cur_max = max(window)
            elif cur_max < v :
                cur_max = v
            
            results.append(cur_max)
            
            # 최댓값이 윈도우에서 빠지면 초기화
            if cur_max == window.popleft() :
                cur_max = float('-inf')
            
        return results