def solution(n):
    answer = 0
    add = n-2
    if add <= 0 : # 추가해야할 배열개수가 필요없다면 0개 추가
        add = 0
    
    dp = [1,2] + [0]*add

    # i번째의 직사각형 배치 갯수는 i-1번째 경우와 i-2번째 경우를 더한 값이다
    for i in range(2,n) :
        # 해당 값을 1000000007로 나눈 나머지를 구한다
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    answer = dp[n-1] # n번째 경우의 수 구함
    # print(answer)

    return answer

n = 4
solution(n)