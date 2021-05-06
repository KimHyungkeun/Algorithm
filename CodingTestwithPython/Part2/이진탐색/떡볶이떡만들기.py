import sys

# 파라메트릭 서치

# 떡 개수 n개와 필요한 떡의 길이 m
n, m = map(int, sys.stdin.readline().split())
# 떡 각각의 길이를 입력
rice_cake = list(map(int, sys.stdin.readline().split()))


# 이진 탐색
def binary_search(array, start, end) :

    while start <= end :

        # 현재 떡 중에서 가장 긴 길이의 떡을 절반으로 가른다
        mid = (start + end) // 2
        print("mid : ", mid)
        total = 0 # 현재까지 누적된 떡의 길이
        for n in array :
            if n > mid :
                total += (n-mid) # 현재 기준으로 정한 길이 이상의 떡들의 길이를 모두 더한다
        print("total : ", total)
        if total == m : # 요구하는 길이대로 나오면 그대로 함수 종료
            return mid
        
        elif total > m : # 만약 요구길이보다 더 길게 나오면, 현재 기준길이를 시작점으로 하여 다시 길이재조정한다
            start = mid + 1
        
        else : # 만약 요구길이보다 짧게 나오면, 떡의 끝지점을 현재 기준점으로 가져온다
            end = mid - 1


result = binary_search(rice_cake, 0, max(rice_cake))
print(result)