import sys

# 두 배열을 입력
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

dp = []
# answer = ""

# a,b 배열길이에 각각 +1한 길이만큼의 dp 테이블을 작성한다. 값은 모두 0으로 초기화
for _ in range(len(a)+1) :
    tmp = [""] * (len(b)+1)
    dp.append(tmp)

for i in range(1, len(a)+1) :
    for j in range(1, len(b)+1) :
        # print(a[i], b[j])
        
        # a와 b의 문자열 각각에서 두 철자가 서로 같은 것이라면, 현재위치에서 북서쪽 방향의 대각선쪽의 값에 1을 더한다 
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + a[i-1]
      
 
        # 만약 서로 다르다면, dp테이블 현 위치에서의 왼쪽 값과 윗쪽 값을 비교해 가장 최대값을 넣는다
        else :
            if len(dp[i][j-1]) < len(dp[i-1][j]) :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]


# print(dp)
# cnt = dp[-1][-1]


if len(dp[-1][-1]) == 0 :
    print(0)
else :
    print(len(dp[-1][-1]))
    print(dp[-1][-1])

# 참고 : https://jjangsungwon.tistory.com/37