def solution(cacheSize, cities):
    
    # 캐시 사이즈가 0이면, cities에 담긴 도시갯수 * 5 만큼 계산하여 바로 적용한다
    if cacheSize == 0 :
        answer = len(cities) * 5
        return answer
    
    # 도시가 대소문자를 구분하지 않으므로, 통일성을 맞추기 위해 모두 소문자형태로 바꾼다
    tmp = []
    for c in cities :
        tmp.append(c.lower())
    cities = tmp
 
    time = 0 # 지나간 시간
    cache = {} # 현재 담겨있는 도시와 얼마의 시간동안 누적되었는지 확인하기 위한 것

    for c in cities :
        # 만약 스택이 비어있다면, 새로 도시를 추가하고 cache miss이므로 시간을 5만큼 증가시킨다
        if not cache :
            cache[c] = 0
            time += 5
        else :
            # 만약 해당 캐시가 cacheSize를 넘어버렸다면
            if len(cache) > cacheSize :
                # 현재 쌓인 cache 중 가장 앞부분 도시를 삭제한다
                for key in cache.keys() :
                    del cache[key]
                    break

            # c가 이미 있는 경우에는, c의 누적 시간을 다시 0으로 새로 초기화 시킨다     
            # 그리고 그 이외의 도시들의 저장 누적시간은 1씩 증가 시킨다
            if c in cache :
                del cache[c]
                if cache :
                    for key in cache.keys() :
                        cache[key] += 1
                cache[c] = 0
                time += 1 # 이때는 cache hit이므로 시간을 1만큼 증가 시킨다
            
            # 해당 도시가 cache 내에 없을때는 cache에 새로 추가하고 시간을 5만큼 증가시킨다
            else :
                cache[c] = 0
                time += 5
                       
        # print(cache)
    # print(time)
    return time