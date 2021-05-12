# 210512 재도전
def flatlandSpaceStations(n, c):
    c.sort()
    ranges = []
    
    pos = 0
    for i in range(n) :
        if i < c[0] :
            ranges.append(abs(c[0] - i)) # 첫 등장하는 우주정거장 보다도 이전 위치면, 무조건 첫 우주정거장 까지의 거리를 기억한다
        
        elif i > c[-1] :
            ranges.append(abs(c[-1] - i)) # 마지막 등장하는 우주정거장 보다도 이후 위치면, 무조건 마지막 우주정거장 까지의 거리를 기억한다
        
        elif i == c[pos] :
            ranges.append(0) # 해당 우주정거장에 도달하면, 다음 우주정거장의 위치로 pos를 이동한다
            pos += 1
        
        else :
            ranges.append(min(abs(c[pos-1] - i), abs(c[pos] - i))) # 현재 위치에서 이전 우주정거장과 다음 우주정거장 중에서 가장 가까운 거리를 기억한다 
    
    print(ranges)
        
    return max(ranges) # 모든 거리값을 모은 리스트 내에서 가장 최대값을 골라낸다



# def flatlandSpaceStations(n, c):
#     result = []
    
#     c.sort() # 우주 정거장 위치를 오름차순 정렬
#     res = c[0] # 첫 정거장 위치
    
#     # 현재 위치중 가장 가까운 우주정거장 까지의 거리를 구함
#     for idx in range(1, len(c)):
#         result.append(max(res, (c[idx] - c[idx-1])//2))
    
#     # 마지막 우주정거장을 기준으로 했을때의 거리를 구함
#     result.append(max(res, n-1 - c[-1]))
        
#     return max(result)

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
    