def solution(N):
    # write your code in Python 3.6
    answer = []

    # 해당 10진수를 2진수로 바꾼다
    while N != 0 :
        answer.append(str(N % 2))
        N //= 2
    
    # 거꾸로 쌓아올려야하므로 reverse함수를 통해 역순으로 정렬한다
    answer.reverse()
    answer = ''.join(answer)
    
    cnt = 0
    max_cnt = 0  
    # 만약 1이라면 경계선이 되므로, 이때 지금까지 쌓인 cnt를 max_cnt와 비교하여 만약 max_cnt를 넘어선 경우 새로운 max_cnt로 
    for n in answer :
        if n == '1' :
            if max_cnt < cnt :
                max_cnt = cnt
            cnt = 0
        else :
            cnt += 1
    print(max_cnt)
    return max_cnt

N = 1041
solution(N)