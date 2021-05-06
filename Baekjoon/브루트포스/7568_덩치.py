import sys

# 사람 수 n을 지정
n = int(sys.stdin.readline())
people = []

# 키와 몸무게 입력
for _ in range(n) :
    x,y = map(int, sys.stdin.readline().split())
    people.append([x,y,1]) # 처음에는 순위를 1위로 매긴다

for i in range(n) :
    for j in range(n) :
        # 만약 본인보다 덩치 큰 사람이 나타나면, 1위에서 밀려난다
        if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
            people[i][2] += 1

# 출력
for i in range(n) :
    print(people[i][2], end = ' ')