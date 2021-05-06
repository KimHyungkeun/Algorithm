# 210505 풀이
from itertools import combinations
def solution(info, query):
    answer = []
    
    info_dict = {}
    for information in info :
        arr = information.split(" ")
        score = int(arr[-1])
        arr = arr[:-1]
        
        for i in range(5) :
            key = combinations(arr, i)
            
            for case in key :
                case = ''.join(case)
                if case in info_dict :
                    info_dict[case].append(score)
                else :
                    info_dict[case] = [score]
                  
    for key in info_dict.keys() :
        info_dict[key].sort()
    
    # print(info_dict)
    for q in query :
        arr = q.split(" ")
        while "and" in arr :
            arr.remove("and")
        while "-" in arr :
            arr.remove("-")
        # print(arr)
        
        target = int(arr[-1])
        query_key = ''.join(arr[:-1])
        # print(query_key)
        
        if query_key not in info_dict :
            answer.append(0)
        else :
            score_range = info_dict[query_key]
            left = 0
            right = len(score_range)-1

            while left <= right :
                mid = (left + right) // 2

                if score_range[mid] < target :
                    left = mid + 1
                else :
                    right = mid - 1

            answer.append(len(score_range)-left)
        
    return answer


# 정답 코드
# from itertools import combinations
# def solution(info, query):
#     answer = []
#     # 0:개발언어, 1:직군, 2:경력, 3:소울푸드, 4:점수
#     combi_dict = {}
    
#     for information in info :
#         tmp = information.split(" ") # info의 내용을 공백 기준으로 나눈다
#         for i in range(5) : # info에 담긴 전체 내용중 1 ~ 5개 까지를 고르는 경우의 수를 구한다
#             for combi_info in combinations(tmp[:4], i) :  # 점수 부분을 제외한 나머지 부분에 대한 핸들링
#                 sum_info = ''.join(combi_info) # 나머지 부분을 하나의 문자열을 붙인다
#                 # 병합한 문자열을 key로 하고 value를 점수들을 모아놓는 리스트로 설정한다
#                 if sum_info in combi_dict : 
#                     combi_dict[sum_info].append(int(tmp[-1]))
#                 else : 
#                     combi_dict[sum_info] = [int(tmp[-1])]
    
#     # 나중의 이분탐색을 위해 점수들을 각각 오름차순 정렬한다
#     for key in combi_dict.keys() :
#         combi_dict[key].sort()
    
#     print(combi_dict)
    
#     for q in query :
#         combi_command = q.split(" ") # 쿼리를 공백기준으로 먼저 구분한다
#         target = int(combi_command[-1]) # 찾아야할 점수를 따로 분리한다
#         combi_command = combi_command[:-1] # 점수 부분을 제외한 나머지 쿼리또한 독립적으로 분리한다
        
#         while 'and' in combi_command : # 쿼리 내에서 and 부분을 삭제한다 
#             combi_command.remove('and')
#         while '-' in combi_command : # 쿼리 내에서 '-' 부분을 삭제한다
#             combi_command.remove('-')
#         combi_command = ''.join(combi_command) # and와 '-'를 제외한 나머지 쿼리정보를 하나의 문자열로 합병한다
        
#         if combi_command in combi_dict : # 만약 해당 쿼리조합을 key로 하는 것이 combi_dict에 존재한다면
#             scores = combi_dict[combi_command] # 해당 쿼리조합에 해당하는 점수 리스트를 불러온다
            
#             left = 0
#             right = len(scores)-1
            
#             # 이분 탐색을 통해 쿼리내에서 원하는 점수 이상의 영역이 분포하는 곳을 찾아낸다
#             while left <= right :
#                 mid = (left + right) // 2
                
#                 if target > scores[mid] :
#                     left = mid + 1
#                 else :
#                     right = mid - 1
            
#             # 찾아낸 영역 내의 갯수를 answer에 넣는다
#             answer.append(len(scores)-left)

#         # 만약 해당 쿼리조합을 key로 하는 것이 combi_dict에 존재하지 않으면, 0을 answer에 넣는다
#         else :
#             answer.append(0)
    
#     return answer

# 참고 : https://tmdrl5779.tistory.com/122

# 정확성 점수 O, 효율성 점수 X
# def solution(info, query):
#     answer = []
#     table = []
    
#     for i in info :
#         arr = i.split(" ")
#         tmp = [arr[0], arr[1], arr[2], arr[3], str(arr[4])]
#         table.append(tmp)
    
#     for q in query :
#         cmd = q.split(" and ")
#         food = cmd[3].split(" ")[0]
#         score = cmd[3].split(" ")[1]
#         cnt = 0
#         for t in table :
#             flag = False
#             if cmd[0] == t[0] or cmd[0] == '-' :
#                 if cmd[1] == t[1] or cmd[1] == '-' :
#                     if cmd[2] == t[2] or cmd[2] == '-' :
#                         if food == t[3] or food == '-' :
#                             if int(t[4]) >= int(score) or score == '-' :
#                                 flag = True
#                             else :
#                                 continue                        
#                         else :
#                             continue
#                     else :
#                         continue
                        
#                 else :
#                     continue
#             else :
#                 continue
            
#             if flag :
#                 cnt += 1
        
#         answer.append(cnt)
                   
#     # print(table)
#     return answer

# scores = [50,80,150,150,210,260]
# target = 150

# left = 0
# right = len(scores)-1

# # 이분 탐색을 통해 쿼리내에서 원하는 점수 이상의 영역이 분포하는 곳을 찾아낸다
# while left <= right :
#     mid = (left + right) // 2
#     print(left, right, mid)
#     if target > scores[mid] :
#         left = mid + 1
#     else :
#         right = mid - 1