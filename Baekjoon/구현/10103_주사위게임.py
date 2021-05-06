import sys

n = int(sys.stdin.readline())
chang = 100 # 창영이 초기점수 100점
sang = 100 # 상덕이 초기점수 100점

for _ in range(n) :
    a, b = map(int ,sys.stdin.readline().split())
    # 만약 상덕이가 더 높게나왔다면, 창영이는 상덕이 수만큼 감점
    if a < b :
        chang -= b
    # 만약 창영이가 더 높게나왔다면, 상덕이가 창영이 만큼 감점
    elif a > b :
        sang -= a
    
    # 둘다 동점이면 그대로 패스
    else :
        continue

print(chang)
print(sang)