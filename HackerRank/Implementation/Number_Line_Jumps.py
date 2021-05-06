# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    
    flag = False
    for x in range(10001) : # 10000까지 범위를 측정한다
        if x1 + v1*x == x2 + v2*x : # x1과 x2의 캥거루에 대해서 만약 교차지점을 찾게되면 루프문 탈출
            flag = True
            break 
    
    # 만약 교차지점을 찾으면 YES 출력
    if flag :
        return "YES"
    
    # 10000 초과의 범위임에도 만나지 못하면 NO 출력
    else :
        return "NO"