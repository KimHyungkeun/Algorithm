# Complete the gemstones function below.
def gemstones(arr):
    
    # 만약 현재 arr가 딱 1개뿐이라면 해당 바위에서 보석종류 갯수를 골라낸다
    if len(arr) == 1 :
        tmp = arr.pop()
        tmp = set(tmp)
        return len(tmp)
    
    else :

        while len(arr) != 1 :
            # 보석끼리의 교집합을 구해서 모든 요소에 공통적으로 있는 보석종류 갯수를 구한다
            tmp = arr.pop()
            tmp2 = arr.pop()
            inter = set(tmp) & set(tmp2)
            inter = list(inter)
            arr.append(inter)
        
        # 최종적으로 나온 결과에 대해 최종 보석종류 갯수를 구한다
        result = arr.pop()
        print(result)
        return len(result)