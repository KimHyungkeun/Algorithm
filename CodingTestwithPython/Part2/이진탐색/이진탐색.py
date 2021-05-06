# 1. 재귀 함수로 이진탐색 구현
# def binary_search(array, target, start, end) :
#     if start > end :
#         return None
#     mid = (start + end) // 2

#     # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target :
#         return mid
    
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target :
#         return binary_search(array, target, start, mid-1)
    
#     else :
#         return binary_search(array, target, mid+1, end)

# array = [1,3,5,7,9,11,13,15,17,19]
# target = 3

# result = binary_search(array, target, 0, len(array) - 1)
# if result == None :
#     print("No element")
# else :
#     print("index : ",result)

# ---------------------------------------------------------------

#2. 반복문으로 이진탐색 구현
def binary_search(array, target, start, end) :
    
    while start <= end :
        mid = (start + end) // 2

        if array[mid] == target :
            return mid

        elif array[mid] > target :
            end = mid - 1
                   
        else :
            start = mid + 1
    
    return None

array = [1,3,5,7,9,11,13,15,17,19]
target = int(input())

result = binary_search(array, target, 0, len(array) - 1)
if result == None :
    print("No element")
else :
    print("index : ",result)