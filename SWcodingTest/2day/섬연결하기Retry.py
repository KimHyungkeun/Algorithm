# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x : x[2])
#     cnt = 0

#     nodes = []
#     for i in range(len(costs)) :
#             nodes.append(costs[i][0])
#             nodes.append(costs[i][1])
#     nodes = set(nodes)

#     search = []
#     for i in range(len(costs)) :
#         flag = 0
#         if costs[i][0] not in search:
#             search.append(costs[i][0])
#             flag += 1
#         if costs[i][1] not in search :
#             search.append(costs[i][1])
#             flag += 1
        
#         if flag >= 1 :
#             cnt += costs[i][2]
        
#         if len(search) == len(nodes) :
#             break
    
#     nodes = set(nodes)
#     search = set(search)

#     # print(nodes)
#     # print(search)
#     answer = cnt
#     # print(answer)
#     return answer

# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# solution(n, costs)

# ---------------------------------------------------------------------------

# 210119 정답코드
def solution(n, costs) :
    costs.sort(key=lambda i:i[2])
    box = set([0])
    money = 0

    while len(box) != n :
        
        for i in costs :
            # print(box)
            if i[0] in box and i[1] in box :
                continue
        
            if i[0] in box or i[1] in box :
                box.update([i[0], i[1]])
                money += i[2]
                break
    
    # print(money)
    return money

    # print(costs)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)

