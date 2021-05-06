def solution(record):
    id_dict = {}
    result = []
    for r in record :
        # 현재 상황에 대한 로그를 공백 기준으로 나눈다
        log = r.split(" ")
        # 맨 앞 명령어 Enter라면, 해당 ID가 들어왔다는 것을 dict에 표기하고, result에 넣는다
        if log[0] == 'Enter' :
            id_dict[log[1]] = log[2]
            result.append(log[1]+ "," + "in")
        # 맨 앞 명령어 Leave라면, 해당 ID가 나갔다는 것을 dict에 표기하고, result에 넣는다
        elif log[0] == 'Leave' :
            result.append(log[1]+ "," + "out")
        # Change 명령어는 그저 현재 닉네임을 변경하기만 한다
        else :
            id_dict[log[1]] = log[2]
        # print(id_dict)
    
    answer = []
    for r in result :
        # result에 담긴 명령어들을 콤마 기준으로 나눔
        cmd = r.split(",")
        # 해당 result가 입장에 대한 레코드라면, 현재 ID가 쓰는 닉네임과 "님이 들어왔습니다"를 이어붙인 문자열을 추가한다
        if cmd[1] == "in" :
            answer.append(id_dict[cmd[0]]+"님이 들어왔습니다.")
         # 해당 result가 퇴장에 대한 레코드라면, 현재 ID가 쓰는 닉네임과 "님이 나갔습니다"를 이어붙인 문자열을 추가한다
        else :
            answer.append(id_dict[cmd[0]]+"님이 나갔습니다.")
    return answer