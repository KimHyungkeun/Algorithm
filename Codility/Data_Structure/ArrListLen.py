def solution(A):
    # write your code in Python 3.6
    head = 0
    cnt = 0

    while head != -1 :
        head = A[head]
        cnt += 1
    
    return cnt