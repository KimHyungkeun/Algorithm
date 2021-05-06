import sys

# 이진 탐색
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        # 원하는 수를 찾으면 1을 리턴
        if array[mid] == target :
            return 1 
        
        elif array[mid] > target :
            end = mid - 1
 
        else :
            start = mid + 1

    # 못찾으면 0을 리턴
    return 0

# 자연수 n개 만큼의 배열을 설정한다
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

# 자연수 search_n개 만큼의 배열을 설정한다
search_n = int(sys.stdin.readline())
search_arr = list(map(int, sys.stdin.readline().split()))


# search_n개의 각각 요소에 대해서, n개 배열에 있는 숫자인지 확인
for num in search_arr :
    result = binary_search(array, num, 0, len(array)-1)
    print(result)
    



    

