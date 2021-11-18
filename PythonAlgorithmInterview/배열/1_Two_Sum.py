class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        # nums 배열 내에서, 두수의 합이 target이 되는 그 수의 각각의 인덱스를 반환
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)) :
                if nums[i] + nums[j] == target :
                    result = [i,j]
                    break
            if nums[i] + nums[j] == target :
                break
        return result