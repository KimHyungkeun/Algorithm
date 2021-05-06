import sys

# 숫자 입력
n = int(sys.stdin.readline())

# 시작지점은 1이다
start = 1
count = 1 # n까지 가는데 걸리는 최소 count를 구함 
cnt = 6 # 일정 범위를 벗어나면, 벌집의 구멍은 6, 12 ,18 순으로 많아진다

while n > start : # n이 해당하는 범위를 찾을때까지 루프문 반복
    count += 1
    start += cnt
    cnt += 6

print(count)