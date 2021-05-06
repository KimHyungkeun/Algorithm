# Complete the quickSort function below.
def quickSort(arr):

    # left에는 pivot이 된 arr[0]보다 작은 수를 넣고
    # right에는 arr[0]보다 큰 수를 넣는다
    left = []
    equal = [arr[0]]
    right = []
    
    for i in range(1, len(arr)) :

        # arr[0]보다 클때
        if arr[0] < arr[i] :
            right.append(arr[i])
        # arr[0]보다 작을때
        elif arr[0] > arr[i] :
            left.append(arr[i])
        # arr[0]과 같을때
        else :
            equal.append(arr[i])
    
    # 결과값 
    result = left + equal + right
    return result