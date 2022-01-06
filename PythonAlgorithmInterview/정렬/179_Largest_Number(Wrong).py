# 오답
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key = lambda x : x*2, reverse=True)
        
        ans = ''.join(nums)
        
        if int(ans) == 0 :
            ans = '0'
        
        return ans

# 정답
class Solution:
    # 문제에 적합한 비교 함수
    @ staticmethod
    def to_swap(n1: int, n2 : int) -> bool :
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums) :
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]) :
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))