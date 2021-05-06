def solution(n):
    answer = 0

    add = n - 2 # 점화식에 의해 추가로 넣어야할 배열개수
    if add <= 0 : # 주어진 dp테이블 이내이면 0개추가
        add = 0

    dp = [1,2] + [0]*add

    for i in range(2,n) : # i번째 경우의 갯수는 i-1번째와 i-2번째 경우의수의 합이다
        dp[i] = dp[i-1] + dp[i-2]

    answer = dp[n-1] % 1234567 # n번째 경우의 수에서 1234567로 나눈 나머지값을 구함
    print(answer)
    return answer

n = 4
solution(n)