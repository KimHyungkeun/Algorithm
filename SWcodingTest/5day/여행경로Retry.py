# def solution(tickets):
#     answer = []
#     graph = {}
#     ticket_used = {}

#     for ap in tickets :
#         if ap[0] not in graph :
#             graph[ap[0]] = [ap[1]]
#         else :
#             if ap[1] not in graph[ap[0]] :
#                 graph[ap[0]].append(ap[1])
        
#         if tuple(ap) in ticket_used :
#             ticket_used[tuple(ap)] += 1
#         else :
#             ticket_used[tuple(ap)] = 1
    
#     if "ICN" not in graph : # key가 곧 시작점을 의미한다. key에 ICN이 없다면 출발자체가 불가하다
#         return answer
    
#     else :
        
#         all_tour = len(tickets) # 모든 티켓을 다쓴경우
        
#         for key, val in graph.items() :
#             if len(graph[key]) >= 2 :
#                 graph[key].sort()
#             # all_tour += len(graph[key])
        
#         def dfs(graph, start, end, ticket_used) :
#             nonlocal all_tour
            
#             # 현재 노드를 방문 처리
#             if ticket_used[(start, end)] >= 1:
#                 answer.append(end)
#                 ticket_used[(start,end)] -= 1
#                 all_tour -= 1

#             # print(answer)
#             # print(ticket_used, all_tour)
#             if end not in graph :
#                 if all_tour == 0 :
#                     return True

#                 else :
#                     answer.pop()
#                     ticket_used[(start,end)] += 1
#                     all_tour += 1
#                     return False

#             if all_tour == 0 :
#                     return True

#             # print((start,end), end=' ')
#             # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#             for dest in graph[end] :
#                 if ticket_used[(end, dest)] >= 1 :
#                    if dfs(graph, end, dest, ticket_used) :
#                        return True
#                    else :
#                        ticket_used[(start, end)] += 1 # 미방문상태로 해야하므로 티켓수를 다시 증가
            
#             return False
     
#         answer = ["ICN"] # 시작은 무조건 인천에서 시작한다
#         for end in graph["ICN"] :
#             # print(end)
#             if dfs(graph, "ICN", end, ticket_used) : 
#                 break

#             else :
#                 answer = ["ICN"]
#                 all_tour = len(tickets)
  
#         print(answer)
#         return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN","A"], ["A","B"], ["B","A"], ["A","ICN"], ["ICN","A"]]
# tickets = [["ICN","COO"], ["ICN","BOO"], ["COO","ICN"], ["BOO","DOO"]]
# tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]
# tickets = [["ICN", "A"],["ICN", "A"],["ICN", "A"],["A", "ICN"],["A", "ICN"]] 
# tickets = [["ITA","ICN"]]
# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]

# -------------------------------------------------------------------------------------------------------

# from collections import defaultdict


# def solution(tickets):
#     answer = []
#     adj = defaultdict(list)
    

#     for ticket in tickets:
#         adj[ticket[0]].append(ticket[1])

#     print(adj)

#     for key in adj.keys():
#         adj[key].sort(reverse=True)

#     q = ['ICN']
#     while q:
#         tmp = q[-1]

#         if not adj[tmp]:
#             answer.append(q.pop())
#         else:
#             q.append(adj[tmp].pop())
#     answer.reverse()
#     return answer

# tickets = [["ICN","A"],["A","B"],["A","C"],["C","A"],["B","D"]]
# solution(tickets)

# # 참고 https://deok2kim.tistory.com/118

from collections import defaultdict

def solution(tickets):
    answer = []
    adj = defaultdict(list) # 가능한 출발지점을 모두 모음


    for ticket in tickets:
        adj[ticket[0]].append(ticket[1]) # 도착 가능한 도착지를 모두 넣음

    for key in adj.keys():
        adj[key].sort(reverse=True) # 역순정렬(pop으로 인해 가장 top이 알파벳순으로 제일낮은 부분임)
    
    # print(ticket_num)
    # print(adj)
    stack = ["ICN"]
    while stack :

        start = stack[-1] 

        if not adj[start] : # 가능한 도착지가 없다면, answer에 넣는다
            answer.append(stack.pop())
        
        else : # 만약 출발지에 도착가능한 도착지가 있다면, 
               # 사전순으로 순서가 낮은 도착지부터 하나씩 세어본다
            stack.append(adj[start].pop())

    answer.reverse()

    print(answer)
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN","A"],["A","B"],["A","C"],["C","A"],["B","D"]]
solution(tickets)