from itertools import permutations
import sys

# 숫자 입력
n = int(sys.stdin.readline())

# 1부터 n까지의 배열
nums = []
for i in range(1,n+1) :
    nums.append(i)

# 1부터 n까지의 모든순열의 경우의 수를 구함
cases = list(permutations(nums, n))

# 순열 출력
for i in range(len(cases)) :
    for j in range(len(cases[i])) :
        print(cases[i][j],end=' ')
    print()

