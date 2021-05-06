import sys

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())
add = n-5
if add < 0 :
    add = 0
array = [1,1,1,2,2] + [0] * add

# 파도반 수열의 n번째는 n-2와 n-3번째의 합이다
for i in range(5, n) :
    array[i] = array[i-2] + array[i-3]

# n번째 수 구함
print(array[n-1]) 