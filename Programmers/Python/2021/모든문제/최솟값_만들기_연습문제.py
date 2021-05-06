def solution(A,B):

    # A는 오름차순, B는 내림차순 정렬
    # 서로 곱해지는 수의 차가 많이 나도록 해야 최솟값에 근접하게 답을 구할 수 있다.
    A.sort()
    B.sort(reverse=True)
    
    total = 0
    # 곱한 값들을 total 변수에 누적시킴
    for i in range(len(A)) :
        total += (A[i] * B[i])

    return total