def solution(A):
    # write your code in Python 3.6
    
    # 테이프 절삭횟수 P, 총 테이프내의 요소의 합 total
    P = len(A)
    total = sum(A)
    minimum = None # 초기 minimum은 None을 설정

    # 왼쪽부터 차례대로 i번째까지의 합과 i+1부터 끝까지의 합을 이어나갈 것이다
    left = 0
    right = total
    
    for i in range(P-1) :
        # i번째 까지의 합 left, i+1부터 끝까지의 합
        left += A[i]
        right -= A[i]
        # 두 수의 차의 절댓값을 구함
        tmp = abs(left - right)

        # 만약 구한 절대값이 현재의 minimum보다도 작다면 새로 갱신한다
        if minimum == None or tmp < minimum :
            minimum = tmp

    return minimum 