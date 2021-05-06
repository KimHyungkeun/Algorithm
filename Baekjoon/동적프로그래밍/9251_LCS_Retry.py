import sys

# 시간 초과, case_a와 case_b를 집합으로 만들어 교집합을 구한 방식으로 하면 메모리 초과
# a = list(sys.stdin.readline().rstrip())
# b = list(sys.stdin.readline().rstrip())

# # print(a,b)
# case_a = []
# case_b = []

# if len(a) == 0 :
#     None

# elif len(a) == 1 :
#     case_a.append(a[0])

# elif len(a) == 2 :
#     case_a += [a[0], a[1], a[0]+a[1]]

# else :
#     case_a += [a[0], a[1], a[0]+a[1]]
#     for i in range(2, len(a)) :
#         length = len(case_a)
#         for j in range(length) :
#             tmp = case_a[j]+a[i]
#             case_a.append(tmp)


# if len(b) == 0 :
#     None

# elif len(b) == 1 :
#     case_b.append(b[0])

# elif len(b) == 2 :
#     case_b += [b[0], b[1], b[0]+b[1]]

# else :
#     case_b += [b[0], b[1], b[0]+b[1]]
#     for i in range(2, len(b)) :
#         length = len(case_b)
#         for j in range(length) :
#             tmp = case_b[j] + b[i]
#             case_b.append(tmp)

# common = set(case_a) & set(case_b)
# common = list(common)
# common.sort(key = lambda x : len(x))
# print(len(common[-1]))


# 두 배열을 입력
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

dp = []
# a,b 배열길이에 각각 +1한 길이만큼의 dp 테이블을 작성한다. 값은 모두 0으로 초기화
for _ in range(len(a)+1) :
    tmp = [0] * (len(b)+1)
    dp.append(tmp)

for i in range(1, len(a)+1) :
    for j in range(1, len(b)+1) :
        # print(a[i], b[j])
        
        # a와 b의 문자열 각각에서 두 철자가 서로 같은 것이라면, 현재위치에서 북서쪽 방향의 대각선쪽의 값에 1을 더한다 
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        # 만약 서로 다르다면, dp테이블 현 위치에서의 왼쪽 값과 윗쪽 값을 비교해 가장 최대값을 넣는다
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(dp)
print(dp[-1][-1])
        
# 참고 https://kils-log-of-develop.tistory.com/260

