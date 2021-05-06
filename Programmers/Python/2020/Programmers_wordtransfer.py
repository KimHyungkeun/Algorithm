# def solution(begin, target, words):
#     answer = 0
#     root = begin
    
#     if target not in words :
#         return answer
    
#     for i in range(len(words)) :
#         diff_cnt = 0
        
#         for j in range(len(target)) :
#             if root[j] != target[j] :
#                 diff_cnt += 1

#         if diff_cnt == 1 :
#             answer += 1
#             # print(answer)
#             return answer
        
#         else :
#             diff_cnt = 0
#             for j in range(len(root)) :
#                 if words[i][j] != root[j] :
#                     diff_cnt += 1
            
            
#             if diff_cnt == 1 :
#                 answer += 1
#                 root = words[i]

    
#     return answer

def solution(begin, target, words):
    answer  = 0

    if target not in words :
        return answer

    graph = dict()
    graph[begin] = []
    for w in words :
        graph[w] = []

    

    for key, value in graph.items() :
        
        for i in range(len(words)) :
            diff_cnt = 0
            for j in range(len(words[i])) :
                if key[j] != words[i][j] :
                    diff_cnt += 1
            if diff_cnt == 1 :
                graph[key].append(words[i])
        
    # print(graph)
    # print(words)
    other_graph = graph
    # print(graph)



    left_visited, need_visit = list(), list()
    need_visit.append(begin)

    # 왼쪽에서 시작
    while need_visit:
        
        node = need_visit.pop(0)
        if node not in left_visited:
            left_visited.append(node)       
            if target in graph[node] :
                left_visited.append(target)
                break
            need_visit.append(graph[node][0])
        


    print(left_visited)  

    # print(other_graph)
    right_visited, need_visit = list(), list()
    need_visit.append(begin)

    # 오른쪽에서 시작
    while need_visit:
        # print(need_visit)
        node = need_visit.pop(-1)
        if node not in right_visited:
            right_visited.append(node)       
            if target in other_graph[node] :
                right_visited.append(target)
                break
            need_visit.append(other_graph[node][-1])
        
    
    print(right_visited) 

    if len(left_visited) >= len(right_visited) :
        answer = len(left_visited) - 1
    else :
        answer = len(right_visited) -1 
     
    # answer = len(right_visited) - 1
    # print(right_visited) 
    # print(answer)
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# begin = "hit"
# target = "hhh"
# words = ["hhh","hht"]
solution(begin, target, words)