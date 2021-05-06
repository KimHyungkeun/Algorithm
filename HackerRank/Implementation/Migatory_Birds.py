# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    # 새 종류는 1,2,3,4,5가 있다
    bird_dict = {1:0, 2:0, 3:0, 4:0, 5:0}

    # 해당되는 새 종류에 따라 마리수를 올린다
    for n in arr :
        if n in bird_dict :
            bird_dict[n] += 1
    
    # 가장 마리수가 많은 새 별로 내림차순 정렬한다
    sort_dict = sorted(bird_dict.items(), key = lambda x : x[1], reverse=True)

    # 가장 마리수가 많은 새의 타입을 반환
    return sort_dict[0][0]