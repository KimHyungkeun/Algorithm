# 모래시계 모양이 되야하므로
# 1 1 1
# 0 1 0
# 1 1 1
# 모양이 있을때, 위 3X3배열에서 1이 있는곳(즉, 그 위치에 있는 값들)을 모두 더한값을 구한다

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maximum = -999999 # 임의로 최대값을 지정
    for i in range(len(arr)) :
        if i+2 < len(arr) : # 모래시계모양이 될 곳을 지정한다
            for j in range(len(arr[i])) :
                if j+2 < len(arr[i]) : # 모래시계모양대로 해당 지점에 있는 값을 모두 더한다 
                    tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                    if tmp > maximum :
                        maximum = tmp
    
    return maximum
            