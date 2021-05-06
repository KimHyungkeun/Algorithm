import sys

n = int(sys.stdin.readline())

# 인덱스를 1부터 세기위해 n개 배열에 1개를 더 추가한 갯수로 만든다
add = n-1
# 기존 0,1 을 시작점으로 두고, 입력된 n번째 피보나치까지 걸리기위한 배열 개수를 정한다
if add < 0 :
    add = 0

fibonacci = [0,1] + [0]*add

# Fn = Fn-1 + Fn-2
for i in range(n+1) :
    if i >= 2 :
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2] 

print(fibonacci[n])