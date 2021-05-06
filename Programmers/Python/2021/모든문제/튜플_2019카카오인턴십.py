def solution(s):
    answer = []
    s = s[1:-1] # 들어오는 문자열에서 가장 맨 앞뒤의 '{', '}'는 제거
    s = s.split("{")[1:] # 문자열 중에서 "{"로 시작하는것을 기준으로 하여 내부 원소 확인
    # print(s)

    for i in range(len(s)) :
        tmp = [] # 문자열 내의 집합기호내의 숫자들을 담기위한 임시 리스트
        num = "" # 문자열 내의 숫자들만을 따로 표기하기위한 변수
        for j in range(len(s[i])) :
            if '0' <= s[i][j] <= '9' : # 숫자타입의 문자라면 num에 추가
                num += s[i][j]
            elif s[i][j] == ',' : # 쉼표를 발견하면 누적한 num 문자열을 tmp에 추가
                tmp.append(num)
                num = ""
            else :
                continue
        if len(num) >= 1 : # 위 반복문 돈 후, 처리하지 않은 num이 있다면 마저 추가
            tmp.append(num)
        answer.append(tmp)
    # print(answer)
    
    # 리스트로 재정리한 결과를 리스트 길이 순으로 오름차순 정렬
    answer.sort(key = lambda x : len(x))
    
    # result 배열에 처음으로 등장한 숫자에 대해서만 차례대로 입력
    result = []
    for i in range(len(answer)) :
        for j in range(len(answer[i])) :
            if int(answer[i][j]) not in result :
                result.append(int(answer[i][j]))
    
    return result