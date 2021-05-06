import sys

n = int(sys.stdin.readline())

# 만약 추가 갯수가 0미만이라는 것은, 기존 주어진 배열에 새로 추가할 필요가 없다는 뜻이다
add = n-2
if add < 0 :
    add = 0

# 각 n자리의 이친수의 갯수는 피보나치 수열의 형태를 띈다
fiboacci = [1,1] + [0]*add

for i in range(2,n) :
    fiboacci[i] = fiboacci[i-2] + fiboacci[i-1]

print(fiboacci[n-1])