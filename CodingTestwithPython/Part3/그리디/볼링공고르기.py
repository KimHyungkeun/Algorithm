import sys

n, m = map(int, sys.stdin.readline().split()) # 볼링공개수 N, 공 최대무게 M
balls = list(map(int, sys.stdin.readline().split())) # 볼링공 종류

cnt = 0
for i in range(len(balls)-1) :
    for j in range(i+1, len(balls)) :
        if balls[i] != balls[j] : # 서로 다른 무게의 공을 주웠을때만 경우의 수를 올린다
            cnt += 1 

print(cnt)