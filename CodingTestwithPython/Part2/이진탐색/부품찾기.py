import sys

# n개의 원소를 가지는 배열을 입력
n = int(sys.stdin.readline())
n_array = list(map(int, sys.stdin.readline().split()))

# m개의 원소를 가지는 배열 입력
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

# 이진탐색을 위해 오름차순 정렬한다
n_array.sort()

# 이진탐색을 진행하는 함수
def binary_search(array, target, start, end) :
    while start <= end :

        mid = (start + end) // 2

        if array[mid] == target :
            return mid
        
        elif target < array[mid] :
            end = mid - 1
        
        else :
            start = mid + 1

    return None

# m배열 내에 있는 원소가 n배열에 포함되어 있는지를 확인한다
for num in m_array :
    result = binary_search(n_array, num, 0, len(n_array)-1)
    if result == None :
        print("no", end=' ') # 미포함은 no
    else :
        print("yes",end=' ') # 포함은 yes