def solution(m, n, puddles):
    answer = 0
    route = []

    # N+1 * M+1 배열을 만든다
    for _ in range(n+1) :
        row = [0] * (m+1)
        route.append(row)
    
    # 초창기 시작점은 1로 표시한다
    route[1][1] = 1
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            # 시작점은 그대로 패스한다
            if i == 1 and j == 1 :
                continue
            
            # 해당 지역이 웅덩이면 그대로 패스한다.
            # (배열의 인덱싱 상으로는 [n][m] 순서이나, 문제에 나온 본래의 좌표 표기순서를 따라간다면 m(j), n(i) 이다)
            if [j, i] in puddles :
                continue
            
            # 해당 좌표까지 오기까지의 경우의 수는, 왼쪽에서 오른쪽으로 오거나 위에서 아래로 오는 경우의 수이다
            else :
                route[i][j] = route[i][j-1] + route[i-1][j]
            
            # for k in range(len(route)) :
            #         print(route[k])
            
            # print("--------------------------")
    
    # 해당 값을 1000000007로 나눈 나머지값으로 저장한다
    answer = route[n][m] % 1000000007
    return answer

m = 4
n = 3
puddles = [[2,2]]
solution(m, n, puddles)

# 참고 https://sexy-developer.tistory.com/37