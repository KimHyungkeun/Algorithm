def solution(X, Y, D):
    # write your code in Python 3.6

    # 시작점과 끝점 사이의 거리
    length = Y - X

    # 두 수 사이의 거리와 점프당 거리를 나누었을때, 나누어 떨어진다면 해당 몫이 답이다
    if length % D == 0 :
        answer = length // D
    
    # 나누어떨어지지 않는다면, 해당 몫에 1을 더한것이 답이다
    else :
        answer = (length // D) + 1
    
    return answer