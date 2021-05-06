import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

def merge(left, right) :
    result = []

    # left와 right 배열에 적어도 숫자 하나라도 포함될 경우
    while left or right :

        # left와 right 둘다 원소가 하나이상 존재할때
        if left and right :
            if left[0] <= right[0] : # 왼쪽이 작다면 result에 넣음
                result.append(left[0])
                left = left[1:]

            else :
                result.append(right[0]) # 오른쪽이 작다면 result에 넣음
                right = right[1:]

        elif left : # left 배열만 있을 경우, 남은 원소를 다 넣는다
            result.append(left[0])
            left = left[1:]

        elif right : # right 배열만 있을 경우, 남은 원소를 다 넣는다 
            result.append(right[0])
            right = right[1:]

    return result

def merge_sort(array) :
    if len(array) <= 1 :
        return array

    # mid로 중간지점을 택한다
    mid = len(array) // 2
    left = array[:mid] # mid 이전까지의 배열
    right = array[mid:] # mid 이후에서 끝지점 까지의 배열

    # 배열길이 1이 될때까지 배열을 쪼갠다
    l = merge_sort(left) 
    r = merge_sort(right)
    return merge(l, r)


result = merge_sort(array)
print(*result)
