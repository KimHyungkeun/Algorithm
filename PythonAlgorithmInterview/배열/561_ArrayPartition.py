class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # nums 내의 수들중 min(a,b) 페어를 이루었을때, min(a,b) + min(c,d) + ... 값이 가장 최댓값으로 나오는 경우
        total = 0
        for i in range(0, len(nums), 2) :
            total += min(nums[i], nums[i+1])
        
        return total