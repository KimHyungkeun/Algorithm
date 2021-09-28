from collections import deque

def solution(rows, columns, queries):
    answer = []
    cnt = 1
    
    # 숫자 테이블을 형성
    table = []
    for i in range(rows) :
        arr = []
        for j in range(columns) :
            arr.append(cnt)
            cnt += 1
        table.append(arr)
    
    # print(table)
    

    for q in queries :
        # 쿼리 내용은 시작 지점과 끝지점을 가리킴(인덱스 0 시작을 기준으로 재구성)
        start_y, start_x = q[0]-1, q[1]-1
        end_y, end_x = q[2]-1, q[3]-1
        queue = deque()
        # print(start_x, start_y)
        
        i = q[0]-1
        j = q[1]-1
        queue.append(table[i][j])
        j += 1

        # 테두리에 포함된 숫자들을 모은 후, 한칸씩 뒤로 미룬다
        while True :

            if queue and table[i][j] == queue[0]:
                break
   
            if i == start_y and j < end_x :
                queue.append(table[i][j])
                j += 1
            
            elif i == start_y and j == end_x :
                queue.append(table[i][j])
                i += 1
            
            elif i < end_y and j == end_x :
                queue.append(table[i][j])
                i += 1
            
            elif i == end_y and j == end_x :
                queue.append(table[i][j])
                j -= 1
            
            elif i == end_y and j > start_x:
                queue.append(table[i][j])
                j -= 1
            
            elif i == start_y and j == start_x :
                queue.append(table[i][j])
            
            elif i > start_y and j == start_x :
                queue.append(table[i][j])
                i -= 1
            
            else :
                None

            # print(i,j,queue)
        
        # 테두리 행렬에 포함된 내용 중, 가장 작은 값을 찾는다
        queue.appendleft(queue.pop())
        answer.append(min(queue))

        # 미루고 난 후의 결과값을, 다시 재배치 시킨다
        i = q[0]-1
        j = q[1]-1
        while queue :

            if i == start_y and j == start_x :
                table[i][j] = queue.popleft()
                j += 1
   
            elif i == start_y and j != end_x :
                table[i][j] = queue.popleft()
                j += 1
            
            elif i == start_y and j == end_x :
                table[i][j] = queue.popleft()
                i += 1
            
            elif i != end_y and j == end_x :
                table[i][j] = queue.popleft()
                i += 1
            
            elif i == end_y and j == end_x :
                table[i][j] = queue.popleft()
                j -= 1
            
            elif i == end_y and j != start_x:
                table[i][j] = queue.popleft()
                j -= 1
            
            elif i == start_y and j == start_x :
                table[i][j] = queue.popleft()
            
            elif i != start_y and j == start_x :
                table[i][j] = queue.popleft()
                i -= 1
            
            else :
                None

    # 결과 값 리턴
    return answer