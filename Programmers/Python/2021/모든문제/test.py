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