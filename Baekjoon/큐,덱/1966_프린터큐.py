from collections import deque
import sys

# 테스트 케이스 수 입력
num = int(sys.stdin.readline())

for _ in range(num) :
    # 배열갯수 n과 찾으려는 인덱스 m을 입력
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    queue = []
    # 큐에 요소들을 넣는다
    for i in range(n) :
        queue.append([arr[i], i])

    
    
    # print(queue)
    # maximum = max(queue)
    # print(maximum[0])

    # 몇번째로 출력되는지 카운트 하기 위함
    count = 0

    # 해당 큐에서 가장 우선순위인 출력물을 찾음
    maximum = max(queue)

    # print("max_value : ", arr[m])
    # print("max_idx : ", m)

    # 출력순서에 사용자가 선택한 문서이면서, 그 문서가 프린터 대기열에서 가장 앞쪽에 있을때까지 루프문 반복 
    while queue[0][0] != arr[m] or queue[0][1] != m or maximum[0] != arr[m]:
        # print(queue)
        if queue[0][0] == maximum[0] :
            count += 1
            queue.pop(0)
            maximum = max(queue)
        
        else :
            queue.append(queue.pop(0))

    # 찾았기 때문에 +1을 더해준다
    print(count+1)
        

    
