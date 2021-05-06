import sys

# 테스트 케이스 입력
t = int(sys.stdin.readline())

for _ in range(t) :
    # 배열내의 요소 갯수 n을 입력하고, 요소들 또한 공백을 기준으로 띄어서 입력받는다
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    # 배열 내 요소 합 
    print(sum(arr))