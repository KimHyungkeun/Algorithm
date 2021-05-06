array = [5,7,9,0,3,1,6,2,4,8]

#버블 소트
# for i in range(len(array)) :
#     for j in range(len(array)-1, i, -1) :
#         if array[j-1] > array[j] :
#             array[j-1], array[j] = array[j], array[j-1]

# 선택 소트
# for i in range(len(array)) :
#     mini = i
#     for j in range(i+1, len(array)) :
#         if array[mini] > array[j] :
#             mini = j
#     array[mini], array[i] = array[i], array[mini]

# 삽입 소트
# for i in range(1, len(array)) :
#     for j in range(i, 0, -1) :
#         if array[j-1] > array[j] :
#             array[j-1], array[j] = array[j], array[j-1]
#         else :
#             break 

# 머지 소트
# def merge(left, right) :
#     result = []

#     while left or right :
#         if left and right :
#             if left[0] < right[0] :
#                 result.append(left[0])
#                 left = left[1:]
#             else :
#                 result.append(right[0])
#                 right = right[1:]
        
#         elif left :
#             result.append(left[0])
#             left = left[1:]
#         else :
#             result.append(right[0])
#             right = right[1:]

#     return result

# def merge_sort(arr) :
#     if len(arr) <= 1 :
#         return arr
    
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]

#     l = merge_sort(left)
#     r = merge_sort(right)
#     return merge(l,r)

# array = merge_sort(array)

# 퀵 소트
# def quick_sort(arr, start, end) :
#     if start >= end :
#         return 
    
#     pivot = start
#     left = start+1
#     right = end
    
#     while left <= right :
#         while left <= right and arr[pivot] >= arr[left] :
#             left += 1
        
#         while left <= right and arr[pivot] <= arr[right] :
#             right -= 1
        
#         if left <= right :
#             arr[left], arr[right] = arr[right], arr[left]
        
#         else :
#             arr[pivot], arr[right] = arr[right], arr[pivot]
    
#     quick_sort(arr, start, right-1)
#     quick_sort(arr, right+1, end)

# quick_sort(array, 0, len(array)-1)

# 힙 소트

# def heapify(arr, idx, n) :
#     left = idx * 2
#     right = idx * 2 + 1
#     s_idx = idx

#     if left <= n and arr[s_idx] <= arr[left] :
#         s_idx = left
#     if right <= n and arr[s_idx] <= arr[right] :
#         s_idx = right
#     if idx != s_idx :
#         arr[idx], arr[s_idx] = arr[s_idx], arr[idx]
#         return heapify(arr, s_idx, n)

# def heap_sort(arr) :
#     n = len(arr)
#     arr = [0] + arr

#     for i in range(n, 0, -1) :
#         heapify(arr, i, n)
    
#     for i in range(n, 0, -1) :
#         arr[1], arr[i] = arr[i], arr[1]
#         heapify(arr, 1, i-1)
    
#     return arr[1:]

# array = heap_sort(array)
print(array)


