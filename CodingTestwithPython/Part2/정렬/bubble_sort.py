import sys

# 배열 갯수 n을 입력하고 n개의 원소를 넣음
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

# 오름차순으로 배열을 정렬 
for i in range(len(array)) :
    for j in range(len(array)-1, i, -1) :
        if array[j-1] > array[j] :
            array[j-1], array[j] = array[j], array[j-1]

# 출력
for arr in array :
    print(arr, end=' ')