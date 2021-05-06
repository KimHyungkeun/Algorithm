def solution(participant, completion):
    answer = ''
    
    # 참가자들을 입력 (참가자 이름에 따라 인원수를 측정한다) 
    participant_dict = {}
    for player in participant :
        if player not in participant_dict :
            participant_dict[player] = 1
        else :
            participant_dict[player] += 1
    
    # 결승점에 도달할 경우 dict에 등록된 인원수를 하나씩 뺀다
    for player in completion :
        participant_dict[player] -= 1
    
    # 동명이인이 있다면 결승점에 도달해도 인원수 1이 남아있으므로, 그선수가 완주하지 못한선수다
    for key,val in participant_dict.items() :
        if val == 1 :
            answer = key
            break

    return answer