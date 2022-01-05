def solution(sizes):
    answer = 0
    weights = []
    heights = []

    # 세로가 가로길이보다 길면, 두 길이를 서로 swap 시킨다
    for s in sizes :
        if s[0] < s[1] :
            s[0], s[1] = s[1], s[0]
        weights.append(s[0])
        heights.append(s[1])
    
    # 가로길이 중 가장 최대값과 세로길이 중 가장 최대값을 구하여 모든 명함을 담을 수 있는 최소 지갑 크기를 구한다
    answer = max(weights) * max(heights)
    return answer