# 210329 풀이
import sys

# 삼각형 변의 갯수 입력
n = int(sys.stdin.readline())

# 삼각형에 들어갈 수들을 입력
tri = []
for _ in range(n) :
    num = list(map(int, sys.stdin.readline().split()))
    tri.append(num)

# 첫 dp는 맨 꼭대기의 수로 지정
dp = [tri[0][0]]
for i in range(1,n) :
    # i번째에 대한 계산을 끝마치고나면 tmp에 담긴 내용을 dp에 새로 갱신
    tmp = []
    for j in range(len(tri[i])) :
        # 삼각형 맨 앞자리면, 지난 dp에서의 앞자리수와 더함
        if j == 0 :
            tmp.append(tri[i][j] + dp[0])
        # 삼각형 맨 뒷자리면, 지난 dp에서의 맨 뒷자리수와 더함
        elif j == len(tri[i])-1 :
            tmp.append(tri[i][j] + dp[-1])
        # dp의 인접한 두 수중, 가장 최댓값인것을 골라 현재의 tri숫자와 더함
        else :
            tmp.append(max(dp[j-1], dp[j]) + tri[i][j])
    dp = tmp

print(max(dp))

# import sys

# # 삼각형 크기 n을 입력
# n = int(sys.stdin.readline())

# triangle = []
# # 순차적으로 +1씩 하여 변의 길이가 증가한다
# for i in range(n) :
#     angle = list(map(int, sys.stdin.readline().split()))
#     triangle.append(angle)

# # print(triangle)

# # 삼각형크기가 1이면, 그 숫자가 가장 max값이 된다
# if n == 1 :
#     print(angle[0])

# else :
#     # 누적된 summary 값들이 담긴 배열이다

#     final_result = [triangle[0]]
#     for i in range(1,n) :
#         # 도중도중의 계산결과를 저장하기 위한 배열
#         result = []
#         for j in range(len(triangle[i])) :
#             if j == 0 : # 만약 끄트머리 이면, 해당 수에 대해서만 덧셈을 실시
#                 result.append(triangle[i][j] + final_result[0][0])
            
#             # 만약 끄트머리의 수라면, 해당 수에 대해서만 덧셈을 실시
#             elif j == len(triangle[i]) - 1 :
#                 result.append(triangle[i][-1] + final_result[0][-1])
            
#             # 삼각형 내부 공간에서는 덧셈의 경우 중, 최대값이 될만한 수들만 집어넣는다
#             else :
#                 result.append(max(triangle[i][j] + final_result[0][j], triangle[i][j] + final_result[0][j-1]))


#         # 새 계산결과를 저장하기위해, 이전 저장목록을 지우고 새 목록을 추가    
#         final_result.pop()
#         final_result.append(result)

#     # 최종 결과들 중에 가장 최댓값을 선택
#     print(max(final_result[0]))
    



            
