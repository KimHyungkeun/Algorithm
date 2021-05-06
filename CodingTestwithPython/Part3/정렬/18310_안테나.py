import sys

n = int(sys.stdin.readline())

# 안테나는 집이 존재하는 위치에만 설치 가능하다
home = list(map(int , sys.stdin.readline().split()))
home.sort() # 집 위치를 오름차순으로 정렬

# 집 배열에서 중간지점에 놓아야, 모든 집까지의 거리의 총합이 최소가 된다
mid = len(home) // 2

# 집이 짝수개이면, mid에서 한 집 이전의 집을 선택
if len(home) % 2 == 0 :
    print(home[mid-1])

# 집이 홀수이면, mid를 선택
else :
    print(home[mid])

# https://coding-food-court.tistory.com/93
