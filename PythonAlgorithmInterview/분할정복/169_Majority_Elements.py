class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        # 숫자 종류를 입력
        for n in list(set(nums)) :
            num_dict[n] = 0
        
        # 숫자별 등장 빈도수를 측정
        for key in num_dict.keys() :
            num_dict[key] = nums.count(key)
        
        # 가장 많이 등장하는 숫자를 리턴
        max_key = max(num_dict.items(), key = lambda x : x[1])
        return max_key[0]


# 분할정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums :
            return 
        if len(nums) == 1 :
            return nums[0]
        
        mid = len(nums) // 2
        a = self.majorityElement(nums[:mid])
        b = self.majorityElement(nums[mid:])
        
        if nums.count(a) > mid :
            return a
        else :
            return b