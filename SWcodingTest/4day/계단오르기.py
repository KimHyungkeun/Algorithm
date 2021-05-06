import sys 

n = int(sys.stdin.readline())
add = n-2
if add < 0 :
    add = 0

# 1층올라가는 방법 1개, 2층올라가는 방법 2개
stairs = [1,2] + [0]*add

# i번째까지 올라가는 방법은 i-1번째 방법수 + i-2번째 방법수이다
for i in range(2, n) :
    stairs[i] = stairs[i-1] + stairs[i-2]

print(stairs[n-1])

# https://level.goorm.io/exam/43083/%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0/quiz/1