def solution(participant, completion):
    answer = ''
    
    # 동명이인 판별을 위해 dict 자료형을 선언
    participant_dict = {}

    # 참가자 이름과 인원수를 기록한다. 즉, 동명이인이면 2명이 될수 있다
    for player in participant :
        if player not in participant_dict :
            participant_dict[player] = 1
        else :
            participant_dict[player] += 1
    
    # 완주한 사람에 대해서는 -1씩 뺀다. 동명이인 중 한명은 통과를 못한것이므로 1이 그대로 남을것이다
    for player in completion :
        participant_dict[player] -= 1
    
    # 완주하지 못한 1인은 키값이 1로 되어있다. 그 사람이 미완주자이다
    for key,val in participant_dict.items() :
        if val == 1 :
            answer = key
            break

    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42576