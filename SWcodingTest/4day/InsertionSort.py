import sys

# 배열에 n개의 숫자를 집어넣고, step단계째에 나타날 배열상태를 보여준다
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
step = int(sys.stdin.readline())

# 삽입정렬
for i in range(1, step+1) :
    for j in range(i,0,-1) :
        if array[j-1] > array[j] :
            array[j-1], array[j] = array[j], array[j-1]
            

for num in array :
    print(num, end=' ')

# https://level.goorm.io/exam/43085/insertion-sort/quiz/1