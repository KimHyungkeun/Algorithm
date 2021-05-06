def solution(A, K):
    # write your code in Python 3.6

    # 배열이 비어있다면 그대로 반환
    if not A :
        return A

    # K번동안 top쪽의 요소를 bottom으로 가져온다
    for _ in range(K) :
        A.insert(0, A.pop())
    
    return A