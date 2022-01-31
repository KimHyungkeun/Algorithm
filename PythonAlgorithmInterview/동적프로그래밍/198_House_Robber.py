import collections

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 집이 없으면 0, 집이 2개 이하면 가장 돈이 많은 집으로
        if not nums :
            return 0
        if len(nums) <= 2 :
            return max(nums)
        
        # 정렬된 딕셔너리 형태 (형태는 튜플 형식)
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)) :
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]