from collections import deque

n, m = map(int, input().split()) # n까지의 오름차순 배열에서, m개의 수를 선택
select_ele = list(map(int, input().split())) # 선택한 m개의 숫자 목록들
array = deque([])

for i in range(1, n+1) :
    array.append(i) # 1 ~ n까지 오름차순으로 배열 설정

cnt = 0 # 연산의 횟수

for num in select_ele :
    # print(array)
    select_idx = array.index(num) # 해당 수의 위치(인덱스)

    left_range = select_idx # 해당 수를 기준으로 왼쪽방향으로 0까지가는데 걸리는 거리
    right_range = len(array) - select_idx # 해당 수를 기준으로 오른쪽방향으로 0까지가는데 걸리는 거리

    if left_range <= right_range : # 왼쪽 거리가 짧을 경우
        for _ in range(left_range) :
            array.append(array.popleft()) # 맨 앞쪽 수를, 맨 뒷쪽으로 보냄
            cnt += 1
        array.popleft() # 선택한 수를 찾으면, 큐에서 제거

    else :
        for _ in range(right_range) : # 오른쪽 거리가 짧을 경우
            array.insert(0, array.pop()) # 맨 뒤쪽 수를, 맨 앞쪽으로 보냄
            cnt += 1
        array.popleft() # 선택한 수를 찾으면, 큐에서 제거

print(cnt)
        
      




