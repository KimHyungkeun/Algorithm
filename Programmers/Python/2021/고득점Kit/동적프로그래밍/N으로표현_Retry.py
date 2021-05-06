# from collections import deque

# def solution(N, number):
#     answer = -1
#     cases = deque()
#     cases.append(N)

#     if number in cases :
#         answer = 1
#         # print(answer)
#         return answer

#     for i in range(2,9) :
#         length = len(cases)
#         while length != 0 :
#             tmp = cases.popleft()
#             cases.append(tmp+N)
#             cases.append(tmp*N)
#             cases.append(tmp-N)
#             cases.append(tmp//N)
#             # print(cases)
#             if number in cases :
#                 answer = i
#                 # print(answer)
#                 return answer
#             length -= 1
#         cases.append(int(str(N)*i))
        

#     # print(answer)
#     return answer

# def solution(N, number):
#     answer = -1
#     DP = []

#     for i in range(1, 9):
#         # 주어진 N을 i번 이어 붙인다
#         num_set = { int(str(N) * i) }

#         for j in range(0, i - 1):
#             # j번째의 DP를 확인
#             for x in DP[j]:
#                 # j번째 DP와 끝자락의 DP에 대해서 서로 사칙연산을 모두 수행한다
#                 for y in DP[-j - 1]:
#                     num_set.add(x + y)
#                     num_set.add(x - y)
#                     num_set.add(x * y)

#                     if y != 0:
#                         num_set.add(x // y)
#                     # print(num_set)
#                     # print(x, y)
#             # print(DP)

#         # 만약 현재의 num_set에 찾으려는 number가 존재한다면, N을 i번 사용했을때 원하는 number가 있다는 것이다
#         if number in num_set:
#             # print(num_set)
#             return i

#         DP.append(num_set)

#     return answer

# 참조 https://blog.naver.com/PostView.nhn?blogId=jaeyoon_95&logNo=221869365904&parentCategoryNo=&categoryNo=50&viewDate=&isShowPopularPosts=true&from=search

def solution(N, number):
    answer = -1
    DP = []
    
    for i in range(1, 9) :
        num_set = { int(str(N) * i) }
        
        for j in range(0, i-1) :
            
            for x in DP[j] :
                for y in DP[-j-1] :
                    num_set.add(x+y)
                    num_set.add(x-y)
                    num_set.add(x*y)
                    
                    if y != 0 :
                        
                        num_set.add(x//y)
        if number in num_set :
            return i
            
        DP.append(num_set)
    
    return -1

N = 5
number = 12
solution(N, number)