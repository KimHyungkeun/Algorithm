# Complete the findMedian function below.
def findMedian(arr):

    # 오름차순 정렬해서, 가장 중간값을 구한다
    arr.sort()
    mid = len(arr) // 2
    
    return arr[mid]