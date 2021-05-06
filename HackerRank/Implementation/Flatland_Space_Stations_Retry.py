# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    result = []
    
    c.sort() # 우주 정거장 위치를 오름차순 정렬
    res = c[0] # 첫 정거장 위치
    
    # 현재 위치중 가장 가까운 우주정거장 까지의 거리를 구함
    for idx in range(1, len(c)):
        result.append(max(res, (c[idx] - c[idx-1])//2))
    
    # 마지막 우주정거장을 기준으로 했을때의 거리를 구함
    result.append(max(res, n-1 - c[-1]))
        
    return max(result)

    # 아래는 틀린 코드
    # idx = 0
    # for i in range(n) :

    #     if i in c :
    #         result.append(0)
    #     elif i <= c[0] :
    #         result.append(c[0]-i)
    #     elif i >= c[-1] :
    #         result.append(i-c[-1])
        
    #     else :
    #         if abs(i-c[idx]) < abs(i-c[idx+1]) :
    #             result.append(abs(i-c[idx]))
    #         else :
    #             result.append(abs(i-c[idx+1]))
    #     if 1 <= idx <= len(c)-1 :
    #         if i > c[idx] :
    #             idx += 1
    #     print(idx)
            
          
    # return max(result)
    