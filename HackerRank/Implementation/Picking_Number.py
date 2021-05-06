def pickingNumbers(a):
    # Write your code here

    # 배열 내에 2가지 서로다른 수들 만이 들어가야하며, 서로다른 두 수의 차는 1이하여야한다.

    a.sort() # 오름차순 정렬
    max_length = 0 # 위 조건을 만족하는 최대 배열의 길이
    answer = [a[0]] # 배열에 가장 첫번째 요소를 집어 넣는다

    for i in range(1, len(a)) :
        # 두 수의 차가 1이하이면 배열에 추가한다
        if abs(answer[-1] - a[i]) <= 1 :
            answer.append(a[i])

        # 만약 현재의 max_length보다 더 길이가 길다면 새로운 길이로 갱신한다
        else :
            if max_length < len(answer) :
                max_length = len(answer)
            answer = [a[i]]

        # 만약 배열내의 숫자 종류가 3종류를 넘어가면 방금 들어갔던 수를 잠시 pop시킨다
        if len(set(answer)) > 2 :
            tmp = answer.pop()

            # 만약 현재의 max_length보다 더 길이가 길다면 새로운 길이로 갱신한다
            if max_length < len(answer) :
                max_length = len(answer)
            
            # 배열에 pop시켰던 수를 다시 집어넣는다
            answer = [tmp]
    
    # 만약 현재의 max_length보다 더 길이가 길다면 새로운 길이로 갱신한다
    if max_length < len(answer) :
        max_length = len(answer)
    return max_length