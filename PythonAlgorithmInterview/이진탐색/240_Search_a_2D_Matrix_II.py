class Solution:

    # 2차원 배열에서 target이 존재하는지 확인한다
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix :
            left = 0
            right = len(arr)-1
            
            while left <= right :
                mid = (left + right) // 2
                
                if arr[mid] == target :
                    return True
                
                elif arr[mid] < target :
                    left = mid + 1
                
                else :
                    right = mid - 1
        
        return False