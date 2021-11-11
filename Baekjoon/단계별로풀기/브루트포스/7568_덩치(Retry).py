import sys

n = int(sys.stdin.readline())

people = []
for _ in range(n) :
    # 기본적으로 해당 덩치는 1위라고 가정한다
    x,y = map(int, sys.stdin.readline().split())
    people.append([x,y,1])

for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        # 만약, 본인보다 키와 몸무게가 더 많이나가는 인원이 오면 순위가 밀린다
        if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
            people[i][2] += 1

for p in people :
    print(p[2],end=' ')