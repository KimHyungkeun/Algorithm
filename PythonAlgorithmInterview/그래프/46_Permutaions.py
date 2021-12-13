from itertools import permutations

# 방법 1 : itertools 이용
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        result = list(permutations(nums, len(nums)))
        
        for r in result :
            ans.append(list(r))
        
        return ans

# 방법 2 : dfs 사용
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        prev_elements = []
        
        def dfs(elements) :
            if len(elements) == 0 :
                results.append(prev_elements[:])
            
            for e in elements :
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        
        dfs(nums)
        return results