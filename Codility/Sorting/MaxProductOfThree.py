def solution(A):
    # write your code in Python 3.6
    A.sort()

    # 정렬된 리스트에서, 뒷쪽부터 차례대로 3개의 값을 곱한값과, 첫째 둘째값을 곱하고나서 마지막 값을 곱한값을 서로 비교하여 더 큰 수를 return
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])