import sys

n, s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

for i in range(s) :
    mini_idx = i # 가장 맨앞쪽의 위치한 인덱스
    for j in range(i+1, len(array)) :
        if array[mini_idx] > array[j] : # 만약 mini_idx 위치보다 더 작은 값을 가진 인덱스를 가지면
            mini_idx = j # 해당 인덱스를 mini_idx를 갱신한다
    array[i], array[mini_idx] = array[mini_idx], array[i]
    
for num in array :
    print(num, end=' ')

# https://level.goorm.io/exam/43265/selection-sort/quiz/1
