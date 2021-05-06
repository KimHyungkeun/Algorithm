# Complete the equalizeArray function below.
def equalizeArray(arr):

    # 원소 하나하나를 살피기위해 집합 타입으로 변환
    set_arr = set(arr)
    
    # 각 원소별 출현횟수를 담기위한 리스트
    num_cnt = []

    # 각 원소에 대한 출현횟수를 담는다
    for n in set_arr :
        num_cnt.append((n, arr.count(n)))
    
    # 가장 많이 등장한 횟수별로 내림차순 정렬한다
    num_cnt.sort(key = lambda x : x[1], reverse=True)
    # print(num_cnt)

    # 전체 arr길이에서 가장많이 등장한 횟수를 제외하면, 중복되는 원소들만 남겨지기 위해 없어져야할 숫자들의 갯수를 알수있다
    return len(arr) - num_cnt[0][1]