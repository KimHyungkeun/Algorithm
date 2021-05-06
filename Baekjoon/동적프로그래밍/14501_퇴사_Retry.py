import sys

n = int(sys.stdin.readline())
# n일동안의 받은 월급들
dp = [0] * n

schedule = []
# 걸리는 시간 t와 급여 p를 각각 입력한다
for _ in range(n) :
    t, p = map(int, sys.stdin.readline().split())
    schedule.append((t,p))

for i in range(n) :
    # 해당 i일에서 걸리는 상담시간 [i][0]을 더했을때, 퇴사하기 이전이라면
    if i + schedule[i][0] <= n :
        # i번째 날의 급여를 받는다
        dp[i] = schedule[i][1]
        for j in range(i) :
            if j + schedule[j][0] <= i :
                dp[i] = max(dp[i], dp[j] + schedule[i][1])
        print(dp)

print(max(dp))

# 참고 : https://ihatecucumber.tistory.com/15


# import sys

# n = int(sys.stdin.readline())
# DP = []

# schedule = [(0,0)]
# for _ in range(n) :
#     t, p = map(int, sys.stdin.readline().split())
#     schedule.append((t,p))



# for i in range(1, n+1) :
#     day = i
#     total = 0
#     while day <= n :    
#         if day + schedule[day][0] <= n+1 :
#             total += schedule[day][1]
#             day += schedule[day][0]
#             print((i ,total, day))
#         else :
#             break
    
#     DP.append(total)

# print(max(DP))




