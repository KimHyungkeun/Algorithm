from itertools import permutations
def solution(k, dungeons):
    
    # 던전 전체 입장 횟수
    full_try = len(dungeons)
    dungeons = list(permutations(dungeons, full_try))
        
    # 던전 최대 입장 횟수
    max_try = 0
    for d in dungeons :      
        cnt = 0
        full_pirodo = k
        # 던전 입장에 필요한 최소 피로도는 minimum, 던전 입장 후 소모되는 피로도는 require이다
        for minimum_pirodo, require_pirodo in d :
            if full_pirodo < minimum_pirodo :
                break
            full_pirodo -= require_pirodo
            cnt += 1
        
        # 최대한 입장 가능한 경우의 수로 갱신한다
        max_try = max(max_try, cnt)
        if max_try == full_try :
            break
            
    return max_try