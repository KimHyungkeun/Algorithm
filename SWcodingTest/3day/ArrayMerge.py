import sys

# 배열 n과 배열 m을 입력
n, m = map(int, sys.stdin.readline().split())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = list(map(int, sys.stdin.readline().split()))

# 두 배열을 합친 후, 오름차순으로 정렬
merge_arr = arr_n + arr_m
merge_arr.sort()

# 출력
for arr in merge_arr :
    print(arr, end=' ')
