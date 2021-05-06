import sys

n = int(sys.stdin.readline())

# 1의 자리일 경우 계단수는 본인 그 자체이므로 1개씩이다. (0은 정수이므로 제외)
dp = [0,1,1,1,1,1,1,1,1,1] # 0 ~ 9 까지의 계단수 갯수 

for _ in range(n-1) :
    new_dp = [0] * 10 # 각 0~9까지의 계단수가 만들어질 수 있는 경우의 수
    for i in range(10) :
        if i == 0 :
            new_dp[i] = dp[1] # n자리의 0의 갯수는, n-1자리의 1의 개수와 같다
        elif i == 9 :
            new_dp[i] = dp[8] # n자리의 9의 갯수는, n-1자리의 8의 개수와 같다
        else :
            new_dp[i] = dp[i-1] + dp[i+1] # n자리의 나머지 숫자의 갯수는, n-1자리의 i-1번째 갯수 + i+1번째 갯수를 모두 더한 값이다
    
    # 갯수를 구하고 나면, 해당자리수의 총갯수를 담은 배열로 갱신
    dp = new_dp
    # print(dp)

# n자리에서 나올 수 있는 계단수의 경우
answer = sum(dp) % 1000000000
print(answer)

# 참고 : https://velog.io/@seovalue/%EB%B0%B1%EC%A4%80-10844%EB%B2%88-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98-python



