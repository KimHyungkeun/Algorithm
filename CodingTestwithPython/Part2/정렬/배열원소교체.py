import sys

# 배열의 갯수 n, 최대 k번까지 swap 진행
n, k = map(int, sys.stdin.readline().split())

# 배열 a와 b 설정
arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = list(map(int, sys.stdin.readline().split()))

# 배열 a는 오름차순, 배열 b는 내림차순 
# 내림차순 정렬된 배열b가  상대적으로 작은 숫자가 나오는 배열a의 초반부와 바꿔야 초반부 a도 최댓값으로 치환되고 후반부 a도 최대값이 나오게되어 총합이 가능한한 더 커짐
arr_a.sort()
arr_b.sort(reverse=True)

# 최대 k번까지 배열 a와 b의 교체작업 실시
for i in range(k) :
    arr_a[i],arr_b[i] = arr_b[i], arr_a[i]

# 배열a의 총합 
print(sum(arr_a))