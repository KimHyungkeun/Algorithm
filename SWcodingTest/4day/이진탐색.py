import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
answer = 0

# 이진탐색
def binary_search(array, target, start, end) :
    global answer
    while start <= end :
        mid = (start + end) // 2

        if array[mid] == target :
            answer = mid+1
            return True 
        
        elif target > array[mid] :
            start = mid + 1
        
        else :
            end = mid - 1
    
    return False

result = binary_search(array, target, 0, len(array)-1)

if result :
    print(answer)
else :
    print("X")

# https://level.goorm.io/exam/43218/%EC%8A%A4%ED%83%9D-stack/quiz/1