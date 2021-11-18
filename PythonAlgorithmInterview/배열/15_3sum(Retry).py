class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2) :
            left = i+1
            right = len(nums)-1
            
            
            while left < right :
                sums = nums[i] + nums[left] + nums[right]
                if sums < 0 :
                    left += 1
                
                elif sums > 0 :
                    right -= 1
                
                else :
                    if [nums[i],nums[left],nums[right]] not in result :
                        result.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left+1] :
                        left += 1
                    while left < right and nums[right] == nums[right-1] :
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
                
            
        
        return result