import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

target = 1
for x in arr :
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x :
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
