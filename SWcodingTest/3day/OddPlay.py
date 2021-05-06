import sys

# 숫자 n을 입력하고, 현재 n번째 숫자에 있는 홀수들의 갯수를 구함
n = int(sys.stdin.readline())
final = 2*n -1 

# 현재까지의 홀수들의 총 종류를 모두 구한다
total = 0
for i in range(final,-1,-2) :
    total += i

# 마지막 3개의 수의 합을 구한다
print(2*total-1 + 2*(total-1)-1 + 2*(total-2)-1)
