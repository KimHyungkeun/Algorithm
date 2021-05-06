# 반복문
# def binary_search(array, target, start, end) :
#     while start <= end :
#         mid = (start + end) // 2

#         if array[mid] == target :
#             return mid
        
#         elif array[mid] > target :
#             end = mid - 1

#         else :
#             start = mid + 1
    
#     return None

# --------------------------------------------------------

# 재귀함수
def binary_search(array, target, start, end) :
    
    if start > end :
        return None

    mid = (start + end) // 2

    if array[mid] == target :
        return mid
    
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)

    else :
        return binary_search(array, target, mid+1, end)

    
    
array = [0,2,4,6,8,10,12,14,16,18]

n, target = list(map(int, input().split()))

result = binary_search(array, target,0, n-1)
if result == None :
    print("No element")

else :
    print(result + 1)