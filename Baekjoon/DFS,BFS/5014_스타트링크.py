
# 210518 재풀이


































# # 210403
# import sys
# from collections import deque

# # f : 총 층수, s : 현재위치, g : 목표위치, u : 올라가는 층 갯수, d : 내려가는 층 갯수
# f,s,g,u,d = map(int, sys.stdin.readline().split())
# visited = [0] * f

# # 현재위치와 목표위치가 같다면 탐색하지 않아도 됨
# if s == g :
#     print(0)

# else :
#     queue = deque()
#     queue.append(s)
#     depth = 0 # 경우의 수 확인
#     answer = False

#     while queue :

#         length = len(queue)
        
#         while length != 0 :
#             q = queue.popleft()
#             if q == g :
#                 # 방문했다면 1을 넣어서 표기
#                 visited[q-1] = 1
#                 break

#             # f층 이내에 올라갈 수 있는 층이라면, 그 층을 방문
#             if q+u <= f and q+u not in queue and visited[q+u-1] == 0 :
#                 queue.append(q+u)
#                 visited[q+u-1] = 1
            
#             # 1층 보다는 큰 수의 층이라면, 그 층을 방문
#             if q-d >= 1 and q-d not in queue and visited[q-d-1] == 0 :
#                 queue.append(q-d)
#                 visited[q-d-1] = 1
            
#             # 현재 확인가능한 경우의 수에서 1을 제외
#             length -= 1
            
#         depth += 1

#         if visited[g-1] == 1 :
#             answer = True
#             break
        
#     # 최소로 조작가능한 버튼 클릭 갯수
#     if answer :
#         print(depth)

#     # 올라 갈 수 없다면 use the stairs
#     else :
#         print("use the stairs")
 
# ----------------------------------------------------------------------


# import sys
# from collections import deque

# # f : 총 층수, s : 현재위치, g : 목표위치, u : 올라가는 층 갯수, d : 내려가는 층 갯수
# f,s,g,u,d = map(int, sys.stdin.readline().split())
# visited = [0] * (f+1)
# # print(queue)

# # 현재위치와 목표위치가 같다면 탐색하지 않아도 됨
# if s == g :
#     print(0)

# else :
#     queue = deque()
#     queue.append(s)
#     depth = 0 # 경우의 수 확인
#     answer = False 

#     while queue :
#         # 현재 확인할수 있는 총 경우의 수
#         length = len(queue)

#         while length != 0 :
#             q = queue.popleft()
            
#             if q == g :
#                 # 방문했다면 1을 넣어서 표기
#                 visited[q] = 1
#                 answer = True
#                 break

#             # f층 이내에 올라갈 수 있는 층이라면, 그 층을 방문
#             if q + u <= f and visited[q + u] == 0 :
#                 queue.append(q + u)
#                 visited[q + u] = 1
            
#             # 1층 보다는 큰 수의 층이라면, 그 층을 방문
#             if q - d >= 1 and visited[q - d] == 0 :
#                 queue.append(q - d)
#                 visited[q - d] = 1
            
#             # 현재 확인가능한 경우의 수에서 1을 제외
#             length -= 1
        
#         # 만약 원하는 층을 방문했다면 루프문 탈출
#         if answer and length != 0:
#             break
        
#         # 원하는 층만 방문이 안되었다면 루프문 탈출
#         if visited[q] == 0 and sum(visited[1:f+1]) == f-1 :
#             break
        
#         depth += 1
        
#     # 최소로 조작가능한 버튼 클릭 갯수
#     if answer :
#         print(depth)
#     # 올라 갈 수 없다면 use the stairs
#     else :
#         print("use the stairs")
        



   


