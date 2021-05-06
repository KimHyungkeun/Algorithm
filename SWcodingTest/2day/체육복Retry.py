# --------------------------------------------------------

# 210119 정답코드
# def solution(n, lost, reserve) :

#     a = set(lost) & set(reserve)
#     lost = list(set(lost) - a)
#     reserve = list(set(reserve) - a)

#     for i in reserve :
#         if i-1 in lost :
#             lost.remove(i-1)
#         elif i+1 in lost :
#             lost.remove(i+1)
    
#     return n - lost(lost)

# ----------------------------------------------------------

