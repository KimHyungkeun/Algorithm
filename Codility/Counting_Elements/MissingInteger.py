def solution(A):
    # write your code in Python 3.6

    # A 배열의 최댓값 조차 음수이면, 나와야하는 가장 작은 양수는 1이다
    if max(A) < 0 :
        return 1
    
    # A를 집합으로 만든 후, 오름차순 정렬
    A = sorted(list(set(A)))
   
    # 최초로 나오는 양수를 찾아낸다
    for i in range(len(A)) :
        if A[i] > 0 :
            break
    
    # 만약 최초로 나온 양수가 1보다 큰 수라면, 나와야하는 가장 작은 양수는 1이다
    if A[i] != 1 :
        return 1

    # 현재 수와 다음수의 차가 1보다 크게되면 누락된 수가 있다는 뜻이므로, 현재수의 1을 더한값이 답이 된다
    start = i
    for i in range(start, len(A)-1) :
        if A[i+1] - A[i] > 1 :
            return A[i]+1
    
    # 모든 배열이 잘 정렬되어 있다면, 배열내의 최댓값에 1을 더한 값이 나와야 한다
    return A[-1] + 1