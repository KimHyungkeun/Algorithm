# Complete the runningTime function below.
def runningTime(arr):

    # 정렬 과정에서의 swap 횟수를 센다
    cnt = 0
    for i in range(1, len(arr)) :
        pos = i
        for j in range(i-1, -1, -1) :
            # 만약 이전위치의 수가 현재위치 수보다 크다면 두 수를 서로 바꾸고, pos에 담긴 위치또한 새로 갱신한다
            if arr[j] > arr[pos] :
                arr[j], arr[pos] = arr[pos], arr[j]
                j, pos = pos, j
                cnt += 1 # 한번 swap이 일어날때마다 카운트를 올린다
            else :
                break
    
    return cnt