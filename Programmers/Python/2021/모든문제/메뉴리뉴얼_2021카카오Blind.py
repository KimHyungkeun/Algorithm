# 210506 TRY
from itertools import combinations

def solution(orders, course):
    result = []
    
    tmp = []
    for c in course :       
        menu = {}
        for order in orders :
            if len(order) < c :
                continue
            arr = list(combinations(sorted(order),c))
            for a in arr :
                if a not in menu :
                    menu[a] = 1
                else :
                    menu[a] += 1
        if menu :
            max_key = max(menu, key=menu.get)
            max_val = menu[max_key]
            if max_val >= 2 :
                for combi in menu.keys() :
                    if menu[combi] == max_val :
                        tmp.append(combi)
    
    for t in tmp :
        result.append(''.join(t))
    
    result.sort()
    # print(result)
    return result

# from itertools import combinations
# import operator

# def solution(orders, course):
#     result = [] # 최종 결과를 담기위한 리스트
    
#     result_with_cnt = [] # 해당 단품조합의 주문 수까지 같이 나타내기 위한 임시 리스트
#     for c in course :           
#         tmp = {}
#         for o in orders :
#             if (c > len(o)) : # 만약 해당 주문조합 갯수가 현재 course조합 갯수를 초과하면 패스한다 
#                 continue
#             arr = list(map(''.join, combinations(sorted(o), c))) # 해당 주문 조합을 오름차순으로 정렬 후, c개를 고른 조합 종류 후보를 걸러낸다
#             for a in arr :
#                 # 해당 조합에 대한 갯수를 구한다
#                 if a in tmp : 
#                     tmp[a] += 1
#                 else :
#                     tmp[a] = 1

#         # print(tmp)

#         # c개의 조합으로 이루어진 코스가 있을 경우
#         if tmp :
#             max_key = max(tmp, key = tmp.get) # c개의 조합 코스 중, 가장 주문 수가 많은것을 골라낸다
#             # print(max_key)
#             max_val = tmp[max_key] # 해당 조합 코스의 주문수를 저장한다
#             for key in tmp.keys() :
#                 if tmp[key] == max_val :
#                     string = ''.join(key) # 해당 조합을 하나의 문자열로 만들어낸다
#                     result_with_cnt.append((string, max_val)) # (조합종류, 주문수) 형태의 튜플을 result_with_cnt에 추가한다

#     result_with_cnt.sort(key = lambda x : x[1], reverse=True) # 현재 담긴 조합을 내림차순 정렬한다
#     while result_with_cnt and result_with_cnt[-1][1] < 2 : # 최소 주문 수가 2개 이상인 것들만 남을 수 있도록, 조건에 부합하지 않는 조합은 제거한다
#         result_with_cnt.pop()
    
#     for r in result_with_cnt : # 현재 남은 조합 종류들만 result 리스트에 추가한다
#         result.append(r[0])
    
#     result.sort() # 사전순으로 정렬한다
#     # print(result)
#     return result

# 참고 : https://hyeri0903.tistory.com/126

# 17/20 (시간 초과 코드)
# from itertools import combinations
# import operator

# def solution(orders, course):
#     result = []
    
#     string = ""
#     for o in orders :
#         string += o
#     types = list(set(string))
#     types.sort()
    

#     result_with_cnt = []
#     for c in course :
#         maximum = 0
#         arr = list(combinations(types, c))
             
#         tmp = {}
#         for a in arr :
#             for o in orders :
#                 cnt = set(o) & set(a)
#                 if len(cnt) == c :
#                     if a in tmp :
#                         tmp[a] += 1
#                     else :
#                         tmp[a] = 1
#         # print(tmp)
#         if tmp :
#             max_key = max(tmp, key = tmp.get)
#             # print(max_key)
#             max_val = tmp[max_key]
#             for key in tmp.keys() :
#                 if tmp[key] == max_val :
#                     string = ''.join(key)
#                     result_with_cnt.append((string, max_val))

#     result_with_cnt.sort(key = lambda x : x[1], reverse=True)
#     while result_with_cnt and result_with_cnt[-1][1] < 2 :
#         result_with_cnt.pop()
    
#     for r in result_with_cnt :
#         result.append(r[0])
    
#     result.sort()
#     # print(result)
#     return result

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
solution(orders, course)