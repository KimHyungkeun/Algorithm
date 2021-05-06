import sys

n = int(sys.stdin.readline())

# x->y로 전선을 연결한다
tower = []
for _ in range(n) :
    x,y = map(int, sys.stdin.readline().split())
    tower.append((x,y))

# 송전탑을 x쪽 번호를 기준으로 오름차순한다
tower.sort(key=lambda x : x[0])


# 각 원소 하나하나를, 수가 1개인 부분배열로 본다
dp = [1] * n

for i in range(n) :
    for j in range(i) :
        # i번째 수 이전까지의 수들 중, i번째 수보다 작으면서 부분수열의 길이가 긴것을 dp로 설정한다
        if tower[j][1] < tower[i][1] :
            dp[i] = max(dp[i], dp[j]+1)

# 전체 n에서 가장 긴 부분수열의 갯수를 제외한 것이 답이다
print(n - max(dp))






















# ------------------------------------------------------------------------------

# tower = []

# # 송전탑 a,b 사이에 서로 이어진 전깃줄들을 차례대로 입력받는다 
# for _ in range(n) :
#     a, b = map(int, sys.stdin.readline().split())
#     tower.append((a,b))

# # a 송전탑을 기준으로 순서대로 배열해놓는다
# tower.sort(key = lambda x : x[0])
# # print(tower)

# arr = []
# for t in tower :
#     arr.append(t[1])

# # 각 원소 하나하나를, 수가 1개인 부분배열로 본다
# dp = [1] * n

# for i in range(n) :
#     for j in range(i) :
#         # i번째 수 이전까지의 수들 중, i번째 수보다 작으면서 부분수열의 길이가 긴것을 dp로 설정한다
#         if arr[j] < arr[i] :
#             dp[i] = max(dp[i], dp[j]+1)

# print(n-max(dp))

# # 참고 https://claude-u.tistory.com/206