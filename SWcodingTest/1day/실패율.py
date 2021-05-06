def solution(N, stages):
    answer = []
    tmp = [] # 스테이지와 스테이지의 클리어확률을 같이 넣기위한 임시 배열
    player = len(stages)

    for i in range(1,N+1) :
        count = 0
        for n in stages :
            if i-1 < n <= i : # 해당 스테이지까지 도달했으나 깨지 못한사람만을 카운트한다
                count += 1
        if player == 0 : # 만약 해당 스테이지에 도달한 사람이 없으면 0으로 처리한다
            tmp.append((i,0))
        else :
            percent = count / player # 스테이지 도달했으나 못깬사람 / 스테이지에 도달한 선수
            tmp.append((i, percent))
            player -= count
    
    # 실패율을 내림차순으로 정렬한다
    sorted_tmp = sorted(tmp, key=lambda x : x[1], reverse=True)
    
    for i in range(N) :
        answer.append(sorted_tmp[i][0])

    # print(sorted_tmp)

    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4,4,4,4,4]
solution(N, stages)

# https://programmers.co.kr/learn/courses/30/lessons/42889