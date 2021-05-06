# 재도전 210505
from itertools import combinations

def solution(relation):

    row = len(relation) # 테이블 행의 갯수
    col = len(relation[0]) # 테이블 컬럼의 갯수
    
    candidate = []
    for i in range(1, col+1) : # 전체 컬럼 갯수중, 1 ~ col개 까지의 후보키 조합을 골라낸다 
        tmp = list(combinations(range(col), i))
        candidate += tmp
    # print(candidate)
    
    # 유일성 확인
    unique = []
    for c in candidate : # 모든 후보키 조합 중에서
        tmp = []
        for item in relation : # 해당 테이블의 row중에서
            tuple_tmp = []
            for i in c : # 현재 후보키가 가리키는 컬럼 위치들에 대한, val값들을 tmp에 넣는다
                tuple_tmp.append(item[i])
            tmp.append(tuple(tuple_tmp))
        if len(tmp) == len(set(tmp)) : # 그냥 tmp와 집합 형태의 tmp를 비교해서, 만약 길이가 일치한다면 유일성을 만족하는것이다. (set은 중복 값을 담지 않는다)
            unique.append(c)
    # print(unique)
    
    # 최소성 확인
    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            # 두 후보키를 비교해서, 더 적은 키 갯수로 유일성을 판단할 수 있다면, 길이가 더 긴 후보키는 후보에서 제외시킨다
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])) :
                answer.discard(unique[j])
    
    result = len(answer)    
    return result


# 210504 풀이
# from itertools import combinations

# def solution(relation):
#     row = len(relation)
#     col = len(relation[0])
    
#     # 가능한 모든 경우의 수 구하기
#     candidates = []
#     for i in range(1, col+1) :
#         # 컬럼갯수가 col개이면 그 중 i개 만큼을 고르는 조합 종류를 모두 구한다
#         candidates.extend(combinations(range(col),i))
    
    
#     # 유일성 만족
#     unique = []
#     for candi in candidates :
#         # 구한 candi를 중심으로, 각 여러 컬럼 조합들을 구한 후, 해당 컬럼 조합또한 unique 한지 확인
#         tmp = [tuple(item[i] for i in candi) for item in relation]
        
#         # 만약 중복없이 모두 유일성을 만족한다면, 해당 컬럼들 조합만을 추려낸다
#         if len(set(tmp)) == row :
#             unique.append(candi)
    
#     # 최소성 만족
#     answer = set(unique)
#     # print(unique)
#     # print(answer)
#     for i in range(len(unique)) :
#         for j in range(i+1, len(unique)) :
#             if len(unique[i]) == len(set(unique[i]) & set(unique[j])) :
#                 answer.discard(unique[j]) # remove는 삭제하려는 원소가 없으면 keyerror가 발생하나, discard는 삭제하려는 원소가 없어도 에러 발생 없음
#     # print(answer)
#     return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)

# 참고 https://whwl.tistory.com/104