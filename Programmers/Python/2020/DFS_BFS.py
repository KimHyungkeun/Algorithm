# from collections import deque

# graph = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# start_node = 1

# graph = dict()
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']
# start_node = 'A'


# def bfs(graph, start_node):
#     visited = list()
#     need_visit = list()
    
#     need_visit.append(start_node)
    
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
    
#     return visited

# bfs(graph, start_node)


# def dfs(graph, start_node):
#     visited, need_visit = list(), list()
#     need_visit.append(start_node)
    
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)       
#             for i in range(len(graph[node])-1, -1, -1) :
#                 need_visit.insert(0, graph[node][i])
#             # print(need_visit)  
            
#     print(visited)
#     return visited

# dfs(graph, start_node)




# def solution(numbers, target):
#     cnt = 0
#     len_numbers = len(numbers)

#     def operator(idx=0):
        
#         if idx < len_numbers:
#             numbers[idx] *= 1
#             print(idx, numbers[idx])
#             operator(idx+1)

#             numbers[idx] *= -1
#             # print(idx, numbers[idx])
#             operator(idx+1)

#         elif sum(numbers) == target:
#             nonlocal cnt
#             cnt += 1

#     operator()

#     return cnt

# numbers = [1,1,1,1,1]
# target = 3
# solution(numbers, target)

def solution(tickets):
    
    visited = list()
    need_visit = list()
    graph = dict()

    for i in range(len(tickets)) :
        for j in range(len(tickets[i])) :
            if tickets[i][j] not in graph :
                graph[tickets[i][j]] = []
    
    for key,value in graph.items() :
        for i in range(len(tickets)) :
            if tickets[i][0] == key :
                graph[key].append(tickets[i][1])
    
    for key,value in graph.items() :
        graph[key].sort(reverse=True)
    
    print(graph)
    start_node = "ICN"
    need_visit.append(start_node)
    
    while True:
        
        node = need_visit.pop(0)
        visited.append(node)      

        alls = 0
        for key,value in graph.items() :
            if len(graph[key]) == 0 :
                alls += 1
            if alls == len(graph) :
                break
        if alls == len(graph) :
            break      

        if len(graph[node]) != 0 :
            need_visit.append(graph[node][-1])
            graph[node].pop(-1)
        
        else :
            need_visit.append(start_node)
        
       
    
    print(visited)
    return visited

# def solution(tickets):
#     # 1. 그래프 생성
#     routes = dict()

#     for (start, end) in tickets:
#         routes[start] = routes.get(start, []) + [end]  

#     # 2. 시작점 - [끝점] 역순으로 정렬    
#     for r in routes.keys():
#         routes[r].sort(reverse=True)

#     # 3. DFS 알고리즘으로 path를 만들어줌.
#     st = ["ICN"]
#     path = []
    
#     while st:
#         top = st[-1]

#         if top not in routes or len(routes[top]) == 0:
#             path.append(st.pop())
#         else:
#             st.append(routes[top][-1])
#             routes[top] = routes[top][:-1]
    
#     # 4. 만든 path를 거꾸로 돌림.
#     answer = path[::-1]
#     print(answer)
#     return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
solution(tickets)