# 정답 66% : Timeout
def solution(A):
    # write your code in Python 3.6
    A.reverse()
    maxprofit = 0
    for i in range(len(A)-1) :
        maxprofit = max(maxprofit, A[i] - min(A[i+1:]))

    return maxprofit