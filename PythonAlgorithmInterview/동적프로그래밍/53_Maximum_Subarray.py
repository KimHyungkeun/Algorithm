# 메모제이션
# ex) [-2, 1, -3, 4, -1,2,1,-5,4] 가 있으면
# 1) sums = [-2], 다음숫자 1, sums의 마지막 번째 숫자가 0아래이면 그대로 넣음
# 2) sums = [-2,1], 다음숫자 -3, sums의 마지막 번째 숫자가 0이상이면 더해서 넣음
# 3) sums = [-2,1,-2], 다음숫자, 4
# 4) sums = [-2,1,-2,4], 다음숫자 -1
# ...
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)) :
            if sums[i-1] < 0 :
                sums.append(nums[i])
            else :
                sums.append(nums[i] + sums[i-1])
        
        return max(sums)

# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        cur_sum = 0
        
        for num in nums :
            cur_sum = max(num, cur_sum + num)
            best_sum = max(best_sum, cur_sum)
        
        return best_sum