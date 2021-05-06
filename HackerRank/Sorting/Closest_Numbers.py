# Complete the closestNumbers function below.
def closestNumbers(arr):

    # 오름차순 정렬
    arr.sort()
    # 인접한 두 요소를 담기위한 리스트
    result = []
    # 인접한 두 요소의 차이 중, 가장 작은 차이를 담는 변수
    mini_diff = 999999

    for i in range(len(arr)-1) :
        # 두 요소의 차가, mini_diff보다도 작다면 새로 갱신한다
        if abs(arr[i]-arr[i+1]) < mini_diff :
            mini_diff = abs(arr[i]-arr[i+1])
    
    for i in range(len(arr)-1) :
        # 두 인접한 요소의 차이가, mini_diff와 같은 수는 result에 저장한다
        if abs(arr[i]-arr[i+1]) == mini_diff :
            result += [arr[i], arr[i+1]]
    
    return result