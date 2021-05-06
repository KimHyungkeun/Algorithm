# Complete the serviceLane function below.
def serviceLane(n, cases):
    result = []

    # cases에 담긴 배열에 대해서
    for n in cases :
        # width 리스트에서 현재의 n이 가리키는 영역 내에서 가장 최솟값을 result 배열에 저장한다
        tmp = min(width[n[0]:n[-1]+1])
        result.append(tmp)
    
    return result

width = [2,3,1,2,3,2,3,3]