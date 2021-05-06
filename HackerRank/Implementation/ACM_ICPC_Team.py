# Complete the acmTeam function below.
def acmTeam(topic):

    # 인지하고 있는 최대 토픽의 수를 담는 리스트
    max_topic = []

    for i in range(len(topic)-1) :      
        for j in range(i+1, len(topic)) :
            cnt = 0
            # 두 팀이 각각 인지하고 있는 topic 철자 하나하나를 비교한다.
            # 두 팀중 한명이라도 알고있다면, 인지하고 있는 것이다.
            for k in range(len(topic[i])) :
                # 두 팀 모두 모르면, 정말 모르는 것이므로 카운트에서 제외한다
                if topic[i][k] == '0' and topic[j][k] == '0' :
                    continue
                else :
                    cnt += 1
            
            # 두 팀이 인지한 최대 토픽수를 저장한다
            max_topic.append(cnt)
    
    # max_topic에 담긴 최대 토픽 수와, 그 토픽수가 등장하는 빈도수를 구한다
    m = max(max_topic)
    n = max_topic.count(m)
    answer = [m,n]
    return answer