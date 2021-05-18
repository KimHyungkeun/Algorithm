# 210518 재도전
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if n == k :
    print(0)

else :
    q = deque()
    q.append(n)
    length = len(q)
    sec = 0
    visited = [0] * 100001
    while q :
        x = q.popleft()
        length -= 1

        if 0 <= x-1 <= 100000 and visited[x-1] == 0:
            if x-1 == k :
                sec += 1
                break
            q.append(x-1)
            visited[x-1] = 1
        if 0 <= x+1 <= 100000 and visited[x+1] == 0:
            if x+1 == k :
                sec += 1
                break
            q.append(x+1)
            visited[x+1] = 1
        if 0 <= 2*x <= 100000 and visited[2*x] == 0:
            if 2*x == k :
                sec += 1
                break
            q.append(2*x)
            visited[2*x] = 1
         
        if length == 0 :
            sec += 1
            length = len(q)
    
    print(sec)


# # 수빈이 n, 동생 k
# n, k = map(int, sys.stdin.readline().split())
# pos = [0]*100001 # 갈 수 있는 모든 포지션에 대한 위치

# queue = deque() # 현재 초에서 비교가능한 모든 좌표의 수
# queue.append(n) # 첫번째는 본인 자신
# tmp_queue = deque() # 다음 비교할 좌표들을 저장하기위한 임시 덱
# sec = 0

# # 본인과 같은 위치에 있으면 0초걸림
# if n == k :
#     print(sec)

# else :

#     while True :
#         # 모두 비교했다면, 다음 초가 지났을때의 가능한 모든 경우의 수 비교
#         if not queue :
#             queue = tmp_queue
#             tmp_queue = deque()
#             sec += 1
        
#         # 해당 좌표에서 다음 초때 이동 가능한 모든 경우의 수 비교
#         search = queue.popleft()

#         if 0 <= search <= 100000 and pos[search] == 0:
#             pos[search] = 1

#         # 1. n-1로 이동            
#         if 0 <= search-1 <= 100000 and pos[search-1] == 0:
#             tmp_queue.append(search-1)
#             pos[search-1] = 1
        
#         # 2. n+1로 이동
#         if 0 <= search+1 <= 100000 and pos[search+1] == 0:
#             tmp_queue.append(search+1)
#             pos[search+1] = 1
        
#         # 3. n*2 로 이동
#         if 0 <= search*2 <= 100000 and pos[search*2] == 0:
#             tmp_queue.append(search*2)
#             pos[search*2] = 1
        
#         # 만약 해당초에 있다면 출력한다
#         if k in tmp_queue :
#             sec += 1
#             break
        
#     print(sec)        





# ---------------------------------------------------------------------------------------------------------------------------------

# import sys
# from collections import deque


# # 수빈이 위치 n, 동생 위치 k
# n, k = map(int, sys.stdin.readline().split())

# sec = 0 # 지나간 시간
# visit=[0]*1000001
# queue = deque()
# queue.append([n]) # 맨 처음의 수빈의 위치

# while queue :

#     # x-1, x+1, 2*x 일때의 위치정보를 담아두는 임시 큐
#     new_queue = []

#     i = 0

#     while i < len(queue[0]) :
#         # 수빈이가 있는 곳의 위치
#         point = queue[0][i]
#         # 만약 해당 위치로 간적이 없다면, 위치정보에 기록해둔다
#         if visit[point] == 0 :
#             visit[point] = 1
#             if visit[k] == 1 : # 만약 그 위치가 동생이 있는곳이라면 루프문을 탈출한다
#                 break
        
#         # 1. x-1 위치일때의 위치정보를 기록한다
#         if visit[point-1] == 0 and point-1 >= 0:
#             visit[point-1] = 1
#             new_queue.append(point-1)
        
#         # 2. x+1 위치일때의 위치정보를 기록한다
#         if visit[point+1] == 0 and point+1 <= 100000:
#             visit[point+1] = 1
#             new_queue.append(point+1)
        
#         # 3. 2x 위치일때의 위치정보를 기록한다
#         if visit[point*2] == 0 and point*2 <= 100000 :
#             visit[point*2] = 1
#             new_queue.append(point*2)      

#         # 큐에 담겨져있는 모든 위치정보를 조사해본다
#         i += 1


#     # 만약 동생 위치가 발견되어있는 곳이라면 루프문 탈출한다
#     if k in queue[0] :
#         print(sec)
#         break


#     # 아니라면, 이전의 depth의 위치를 제거하고 새로운 위치정보로 갱신한다.
#     queue.popleft() 
#     queue.append(new_queue)
#     sec += 1 # 1초 지나게 한다
    
    

    


