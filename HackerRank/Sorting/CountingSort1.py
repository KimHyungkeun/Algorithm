# Complete the countingSort function below.
def countingSort(arr):
    
    result = []
    
    # 배열 내에서 가장 최대값을 구하고, count배열 내에 0부터 n까지의 등장횟수를 담을 배열을 만든다
    n = max(arr)
    count = [0] * (n+1)
    
    # n이 등장할때마다 그 등장횟수를 하나씩 늘려나간다
    for n in arr :
        count[n] += 1
    
    return count