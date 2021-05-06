import sys

# 배열의 크기 n
n = int(sys.stdin.readline())

for _ in range(n) :
    array = list(map(int, sys.stdin.readline().split()))
    array.sort(reverse=True)
    # 배열중에서 3번째로 큰수를 구해야 한다
    print(array[2])