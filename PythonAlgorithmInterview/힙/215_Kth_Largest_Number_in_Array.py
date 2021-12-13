# 힙소트를 이용해 정렬 후, k번째 값을 구한다
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
   
        def heapify(arr, idx, n) :
            s_idx = idx
            left = idx * 2
            right = idx * 2 + 1
            
            if left <= n and arr[s_idx] >= arr[left] :
                s_idx = left
            
            if right <= n and arr[s_idx] >= arr[right] :
                s_idx = right
            
            if idx != s_idx :
                arr[idx], arr[s_idx] = arr[s_idx], arr[idx]
                heapify(arr, s_idx, n)
        
        def heap_arr(arr) :
            n = len(arr)
            arr = [0] + arr
            
            for i in range(n, 0, -1) :
                heapify(arr, i, n)
            
            for i in range(n, 0, -1) :
                arr[1], arr[i] = arr[i], arr[1]
                heapify(arr, 1, i-1)
            
            return arr[1:]
        
        result = heap_arr(nums)
        
                
        return result[k-1]