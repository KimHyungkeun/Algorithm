import sys
n = int(sys.stdin.readline()) # 배열 원소의 갯수

arr = list(map(int, sys.stdin.readline().split())) # 배열 입력
set_arr = list(set(arr)) # 배열에 담긴 원소 종류들 모음
set_arr.sort() # 원소 종류 모음을  오름차순 정렬

arr_idx = [] # 답을 넣을 공간
idx_storage = {} # 이미 거쳐간 곳이라면, 그 위치를 기억한다

for a in arr :
    if idx_storage.get(a) :# 만약 idx_storage가 기억한 곳이면, 이곳에서 답을 찾아낸다
        arr_idx.append(idx_storage[a])  
        continue

    start = 0
    end = len(set_arr)-1

    # 이분 탐색을 통해 해당 값의 위치를 찾아낸다
    while start <= end : 
        mid = (start + end) // 2

        if set_arr[mid] == a :      
            idx_storage[a] = mid    
            arr_idx.append(idx_storage[a])    
            break

        elif a < set_arr[mid] :
            end = mid - 1
        
        else :
            start = mid + 1

print(*arr_idx)

