import sys

# 오르는 길이 a, 미끄럼 길이 b, 총 막대길이 v
a, b, v = map(int, sys.stdin.readline().split())

# 막대길이와 오르는길이에서 미끄럼 길이를 모두 제외하고, 오르기까지 총 몇번 걸리는지 구한다.
if (v - b) % (a - b) == 0 : 
    day = (v - b) // (a - b)

# 만약 나누어 떨어지지 않으면, 정상까지 하루 더 걸리는 것이다.
else :
    day = (v - b) // (a - b) + 1

print(day)