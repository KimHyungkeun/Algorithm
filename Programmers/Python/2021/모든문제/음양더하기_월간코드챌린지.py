def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)) :
        # sing이 True이면 양수 그대로임
        if signs[i] :
            answer += absolutes[i]
        # sign가 False이면 실제로는 음수임
        else :
            answer -= absolutes[i]
    # 더한 값들을 리턴
    return answer