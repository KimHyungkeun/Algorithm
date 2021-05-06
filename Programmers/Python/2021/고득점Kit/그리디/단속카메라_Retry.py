def solution(routes):
    # 고속도로가 끝나는 지점을 기준으로 정렬한다
    routes.sort(key = lambda x : x[1])
    pos = -100000 # 기본값으로 가장 최소의 값을 둔다
    cnt = 0

    for i in routes :
        # 만약 현재의 카메라 위치가 진입구간보다 더 이전이라면
        if pos < i[0] :
            cnt += 1 # 카메라 개수를 증가시킨다
            pos = i[1] # 해당 고속도로의 끝지점에 카메라를 둔다

    print(cnt)
    return cnt

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)