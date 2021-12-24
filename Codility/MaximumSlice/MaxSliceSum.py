# 정답 69%
def solution(A):
    # write your code in Python 3.6
    left = 0
    right = 0
    maximum = A[0]
    
    while True :
        if left == len(A)-1 and right == len(A)-1 :
            maximum = max(maximum, A[left])
            break
        
        if left == right :
            if right != len(A)-1 :
                right += 1
        
        if sum(A[left:right+1]) > maximum :
            maximum = sum(A[left:right+1])
            if right != len(A)-1 :
                right += 1
        else :
            if left != len(A)-1 :
                left += 1
        
    return maximum

# 정답 : 100%
def solution(A):
    # write your code in Python 3.6
    partSum = 0
    maxSum = -1000000

    for n in A :
        maxSum = max(maxSum, partSum + n)
        partSum = max(0, partSum + n)
        
    return maxSum
# https://nukeguys.tistory.com/188