# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort(key = lambda x : abs(x)) # 해당 수들을 절대값을 기준으로 오름차순한다
    minimum = 1000000000 # 최소값 지정

    for i in range(len(arr)-1) :
        # 만약 i와 i+1번째 원소의 차의 절대값이 현재 minimum보다도 작다면, 새 minimum으로 갱신한다
        if abs(arr[i] - arr[i+1]) < minimum :
            minimum = abs(arr[i] - arr[i+1])
    # print(arr)
    return minimum