# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
 
    for i in range(len(arr)) :
        # 전체 주어진 m의 값에서 i번째 맛의 값을 구입후, 남은 돈으로 다른 맛을 구입할 수 있는지에 대한 여부
        if m - arr[i] in arr :
            # 남은 값으로 다른 맛을 구입하게 된다면, 해당 위치를 반환한다
            j = arr.index(m - arr[i])

            # 만약 같은 위치의 경우, 다른 위치의 맛을 재탐색한다
            if i == j :
                continue
            # 적정 맛을 찾게되면 루프문을 탈출한다
            else :
                break
    
    # 고른 맛을 가격 순서대로 오름차순 정렬한 후, 리턴한다
    result = [i+1, j+1]
    result.sort()
    return result