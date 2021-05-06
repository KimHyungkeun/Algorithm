# Complete the pairs function below.
def pairs(k, arr):
    # arr.sort()
    arr = set(arr) # 각 원소배열은 각각 다른 값이다
    cnt = 0
    
    # 만약 해당 원소에 k를 더했을때, 그 값 또한 arr에 존재하면 카운트를 증가한다
    for n in arr :
        if n + k in arr :
            cnt += 1
    return cnt