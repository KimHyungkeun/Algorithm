import sys

n = int(sys.stdin.readline())

# 피라미드 형식으로 쌓았다해도, 전체 둘레는 결국 변의 길이가 n인 정사각형의 둘레가 된다.
row = n * 4
print(row)