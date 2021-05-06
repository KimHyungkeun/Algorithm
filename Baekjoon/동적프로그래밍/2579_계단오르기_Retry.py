# 210329_여전히 답안보고 풀면 모름
import sys

n = int(sys.stdin.readline())

stairs = [0]

for _ in range(n) :
    step = int(sys.stdin.readline())
    stairs.append(step)

# 계단 1개 : 그 1개만 오르면 됨
if n == 1 :
    print(stairs[1])

# 계단 2개 : 1개 오르기와 1+2개 오르기 중 가장 큰 점수를 고름
elif n == 2 :
    print(max(stairs[1]+stairs[2], stairs[2]))

# 계단 3개 : 1+3 오르기와, 2+3 오르리 중 가장 큰 점수를 고름
elif n == 3 :
    print(max(stairs[1]+stairs[3], stairs[2]+stairs[3]))

# 계단 4개
else :
    # 계단 3개까지의 dp를 모두 구함
    dp = [0, stairs[1], max(stairs[1]+stairs[2], stairs[2]), max(stairs[1]+stairs[3], stairs[2]+stairs[3])]
    
    for i in range(4, n+1) :
        # 현재높이에서 2번째 이전까지의 모든 점수를 더한 값 vs 3번째 이전까지의 모든 점수를 더하고 1번쨰 이전까지의 점수와 현재 계단의 점수까지 모든 더한 값 중 최댓값
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))
    
    print(dp[-1])
# ---------------------------------------------------------------------------------------------------------------------------------

# # 계단수 n
# n = int(sys.stdin.readline())

# # 계단
# stair = [0]
# for _ in range(n) :
#     # 각 계단별 점수
#     step = int(sys.stdin.readline())
#     stair.append(step)

# # 계단수가 하나일 경우
# if n == 1 :
#     print(stair[1])

# # 계단수가 두개일 경우
# elif n == 2 :
#     print(stair[1] + stair[2])

# else :
#     # 나올 수 있는 경우의 수
#     dp = [0]
#     # 첫번째 계단
#     dp.append(stair[1]) 
#     # 첫번째 다음 두번째 계단에 오름
#     dp.append(max(stair[1] + stair[2], stair[2])) 
#     # max(시작위치 + 2칸, 1칸 + 2칸의 경우)
#     dp.append(max(stair[1] + stair[3], stair[2] + stair[3])) 

#     for i in range(4,n+1) :
#         # 전전칸 + 현위치로 올라옴
#         # 현위치에서 전칸을 밟음 + 전전칸 밟은 경우 최대값
#         dp.append(max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]))

#     print(dp[-1])
    


# --------------------------------------------------------------------------------------------------------------------

# import sys

# # 계단수 n
# n = int(sys.stdin.readline())

# # 계단
# stair = []
# for _ in range(n) :
#     # 각 계단별 점수
#     step = int(sys.stdin.readline())
#     stair.append(step)

# # 계단수가 하나일 경우
# if n == 1 :
#     print(stair[0])

# # 계단수가 두개일 경우
# elif n == 2 :
#     print(stair[0] + stair[1])

# else :
#     # 나올 수 있는 경우의 수
#     cases = []
#     # 첫번째 계단
#     cases.append(stair[0]) 
#     # 첫번째 다음 두번째 계단에 오름
#     cases.append(max(stair[0] + stair[1], stair[1])) 
#     # max(시작위치 + 2칸, 1칸 + 2칸의 경우)
#     cases.append(max(stair[0] + stair[2], stair[1] + stair[2])) 

#     for i in range(3,n) :
#         # 전전칸 + 현위치로 올라옴
#         # 현위치에서 전칸을 밟음 + 전전칸 밟은 경우 최대값
#         cases.append(max(cases[i-2] + stair[i], cases[i-3] + stair[i] + stair[i-1]))

#     print(cases[-1])
    


# # print(stair)
# # 참고 https://sungmin-joo.tistory.com/18

