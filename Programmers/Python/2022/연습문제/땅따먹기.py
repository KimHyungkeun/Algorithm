def solution(land):
    answer = 0

    for i in range(1, len(land)) :
        # 각 열에 대해서, 이전 행의 값중 최대값을 더하여 누적시킨다. (단, 같은 열의 값은 더할 수 없다)
        for j in range(4) :
            if j == 0 :
                land[i][j] += max(land[i-1][1:4])
            elif j == 1 :
                land[i][j] += max(land[i-1][0], land[i-1][2], land[i-1][3])
            elif j == 2 :
                land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][3])
            else :
                land[i][j] += max(land[i-1][0:3])
    
    # print(land)
    answer = max(land[-1])
    return answer

# 참고 : https://ssungkang.tistory.com/entry/%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2