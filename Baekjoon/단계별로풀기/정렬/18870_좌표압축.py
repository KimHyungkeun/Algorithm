import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 중복을 제외한 요소들을 모은 후, 내림차순 정렬 
set_arr = list(set(arr))
set_arr.sort(reverse=True)

cnt_dict = {}
for s in set_arr :
    cnt_dict[s] = 0

# i번째 수보다 작은 수는 i+1번째 수부터 끝까지만큼 존재한다
for i in range(len(set_arr)) :
    cnt_dict[set_arr[i]] = len(set_arr) - (i+1)

# 값 출력
for a in arr :
    print(cnt_dict[a], end=' ')







