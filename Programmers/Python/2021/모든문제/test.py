def solution(stones, k):
    answer = 1
    
    left = 1 # 가장 낮은 돌높이
    right = max(stones) # 가장 높은 돌높이
    
    
    while left <= right :
        # print(left, right)
        mid = (left + right) // 2 # 최고와 최저 높이의 돌의 중간값을 구함
        non_stone = 0 # 연속적으로 돌이 몇개가 없는지 카운트
        
        for stone in stones :
            if stone < mid : # 중간높이보다도 낮은 돌이라면 non_stone 증가
                non_stone += 1
            else :
                non_stone = 0 # 그 외의 돌이오면 다시 non_stone 0으로 초기화
            
            if non_stone == k : # k개의 non_stone이 생기면 루프문 탈출
                break
        
        if non_stone == k : # 만약 non_stone이 k개 있다면, right범위를 줄여서 다시 재 탐색
            right = mid - 1
        
        else : # 만약 k개에 미치지 못하면, 현재 건널수있는 인원 answer와 중간높이인 mid중 최댓값을 건널수있는 인원으로 갱신
            answer = max(answer, mid)
            left = mid + 1 

    print(answer)
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)

# from itertools import permutations
# def solution(user_id, banned_id):
#     cnt = 0
#     result = []
    
#     candidate = list(permutations(user_id, len(banned_id)))
#     # print(candidate)
    
#     for candi in candidate :
#         # print(candi)
#         flag = True
#         for i in range(len(banned_id)) :
#             if len(candi[i]) == len(banned_id[i]) :
#                 for j in range(len(banned_id[i])) :
#                     if banned_id[i][j] == '*' :
#                         continue
#                     if candi[i][j] != banned_id[i][j] :
#                         flag = False
#                         break
#                 if not flag :
#                     break
#             else :
#                 flag = False
#                 break
                
#         if flag and set(candi) not in result:
#             result.append(set(candi))
    
#     # print(result)
#     cnt = len(result)
#     return cnt

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]
# solution(user_id, banned_id)