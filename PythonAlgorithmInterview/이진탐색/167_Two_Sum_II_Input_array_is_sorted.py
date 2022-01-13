class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        # 두 수의 합이 target이 되는 값 2개의 각 인덱스 위치를 구한다
        while left <= right :
            if numbers[left] + numbers[right] > target :
                right -= 1
            
            elif numbers[left] + numbers[right] < target :
                left += 1
            
            else :
                break
        
        return [left+1, right+1]