import sys

n = int(sys.stdin.readline())
coordinate = []

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x,y))

# x좌표가 같을 경우 y좌표를 오름차순 정렬하는 룰이 있다.
# 따라서, y좌표 기준으로 먼저 오름차순 정렬 후, x좌표로 정렬한다
sort_cord = sorted(coordinate, key = lambda x : x[1])
sort_cord = sorted(sort_cord, key = lambda x : x[0])

for x,y in sort_cord :
    print(x,y)