# Complete the minimumDistances function below.
def minimumDistances(a):
    # a배열 요소의 인덱스를 담는 딕셔너리
    idx_dict = {} 
    
    minimum = 999999

    # 각 요소가 어느 인덱스에 위치하는지 저장한다
    for i in range(len(a)) :
        if a[i] in idx_dict :
            idx_dict[a[i]].append(i)
        else :
            idx_dict[a[i]] = [i]
    
    
    for key,val in idx_dict.items() :
        # 해당 값이 한번밖에 안나오면 넘어간다
        if len(idx_dict[key]) == 1 :
            continue
        
        # 해당 요소가 등장하는 인덱스사이의 구간 차이를 구해서, 가장 최솟값인 것을 minimum에 저장한다
        else :
            if idx_dict[key][-1] - idx_dict[key][0] < minimum :
                minimum = idx_dict[key][-1] - idx_dict[key][0]
    
    # 만약 모든 원소들이 하나씩밖에 나오지 않으면 -1을 리턴하고, 그 외에는 현재까지 갱신된 최소값을 리턴 
    if minimum == 999999 :
        return -1
    else :
        return minimum