from itertools import combinations

# 방법 1 : itertools 이용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = []
        for i in range(1, n+1) :
            nums.append(i)
        
        result = list(combinations(nums, k))
        
        for r in result :
            ans.append(list(r))
        
        return ans


# 방법 2 : dfs 이용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start, k) :
            if k == 0 :
                results.append(elements[:])
                return
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1) :
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        return results