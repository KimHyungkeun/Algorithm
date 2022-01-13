# 틀린 답
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums :
            return -1
        
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums)-1
        while left <= right :
            mid = (left + right) // 2
            
            if sorted_nums[mid] == target :
                break
            
            elif sorted_nums[mid] < target :
                left = mid + 1
            
            else :
                right = mid - 1
        
        
        for i in range(len(nums)) :     
            if nums[i] == target :
                break
     
        print(i, mid)
        if i == mid :
            return i
        else :
            return i - mid


# 정답
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums :
            return -1
        
        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums)-1
        while left < right :
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right] :
                left = mid + 1
            else :
                right = mid
        
        pivot = left
        
        # 피벗 기준 이진 검색
        left, right = 0, len(nums)-1
        while left <= right :
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target :
                left = mid + 1
            elif nums[mid_pivot] > target :
                right = mid - 1
            else :
                return mid_pivot
        
        return -1