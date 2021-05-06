def solution(arr):
    
    # arr를 오름차순으로 정렬시킨 tmp를 만들면, 그중 가장 left쪽의 수가 최소값을 가진다
    tmp = sorted(arr)
    minimum = tmp[0]
    
    i = 0 
    while i < len(arr) :
        # 해당 번째 수가 arr의 최솟값과 같다면, 그 수를 제거한다
        if arr[i] == minimum :
            del arr[i]
        else :
            i += 1
    
    # arr가 비었다면 [-1]를 리턴
    if not arr :
        arr = [-1]
    
    return arr

arr = [4,3,2,1]
solution(arr)