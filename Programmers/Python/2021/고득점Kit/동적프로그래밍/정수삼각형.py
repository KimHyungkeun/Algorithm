def solution(triangle):
    answer = 0

    # 삼각형높이가 1이면 그 수 자체가 최대값이다
    if len(triangle) == 1 :
        answer = triangle[0][0]
    
    else :
        dp = [triangle[0][0]] # 가장 꼭대기의 수를 dp의 시작으로 둔다

        for i in range(1, len(triangle)) :
            tmp_dp = []
            for j in range(len(triangle[i])) :
                if j == 0 : # i행의 첫번째 수일 경우, i-1행의 첫번째수와 더한다 
                    tmp_dp.append(dp[0] + triangle[i][j])
                elif j == len(triangle[i])-1 : # i행의 마지막번째일 경우, i-1행의 마지막번째 수와 더한다
                    tmp_dp.append(dp[-1] + triangle[i][j])
                else : # i-1행의 j번째와 j-1번째 수중에서, 더했을때 가장 큰값이 나오는 수를 선택하여 dp에 넣는다
                    tmp_dp.append(max(dp[j-1] + triangle[i][j], dp[j] + triangle[i][j]))
            dp = tmp_dp # 새로운 dp로 갱신
            # print(dp)

        # 마지막 행까지 계산을 마친 경우, 그 중 최대값을 구한다
        answer = max(dp)

    print(answer)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)