class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        # nums 배열에서 target이 어떤 인덱스에 위치하는지 확인
        while left <= right :
            mid = (left + right) // 2
            
            if nums[mid] == target :
                return mid
            
            if nums[mid] < target :
                left = mid + 1
            
            else :
                right = mid - 1
        
        return -1