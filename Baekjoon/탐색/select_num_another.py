from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, m = map(int, input().split()) # 데이터 개수 n, 찾고자 하는 수 m
array = list(map(int, input().split()))  # 전체 데이터 입력

# 값이 [m,m] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, m, m)

# 값이 존재하지 않으면 -1 출력
if count == 0 :
    print(-1)

# 값이 존재하면 출력
else :
    print(count)