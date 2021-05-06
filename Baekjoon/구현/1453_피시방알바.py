import sys

# 피시방 자리 갯수는 1~100번 까지다
n = int(sys.stdin.readline())
arr = [0] * 101 # 자리가 1번부터 시작하므로, 인덱스 0을 제외한 1부터 카운트한다

cnt = 0
player = list(map(int, sys.stdin.readline().split()))
for p in player :
    # 자리가 없다면 자리를 차지
    if arr[p] == 0:
        arr[p] = 1
    # 이미 자리가 있다면, 거절횟수를 늘림
    else :
        cnt += 1

print(cnt)