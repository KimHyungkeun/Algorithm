def solution(s):
    # 해당 문자열을 공백 기준으로 나눈다
    arr = s.split(" ")
    new_s = []
    for w in arr : # 새로운 new_s에 공백기준으로 나눈 값들을 집어넣는다(다른 공백문자들까지 전부 포함)
        new_s.append(list(w))
    # print(new_s)

    for i in range(len(new_s)) :
        if new_s[i] == [] : # 별개의 공백에 대한것은 취급하지 않음
            continue
        if '0' <= new_s[i][0] <= '9' : # 첫 문장이 숫자로 시작하면 아무것도 하지 않음
            None
        else :
            if 'a' <= new_s[i][0] <= 'z' : # 첫 문장이 소문자로 시작하면 대문자로 바꿈
                new_s[i][0] = chr(ord(new_s[i][0]) - 32)

        for j in range(1, len(new_s[i])) : # 해당 단어의 두번째 철자부터 마지막 철자까지 검사해서, 대문자인 것들을 소문자로 바꿈
            if 'A' <= new_s[i][j] <= 'Z' :
                new_s[i][j] = chr(ord(new_s[i][j]) + 32)
   
    # print(new_s)
    answer = ''
    for i in range(len(new_s)) :
        # 마지막 번째 문자열에 대해서는 answer에 포함후 따로 공백을 추가로 표기하지 않음
        if i == len(new_s)-1 :
            answer += ''.join(new_s[i])
        # 해당 문자열이 단순한 단어라면, answer에 포함후에 공백까지 포함한다
        elif new_s[i] != ' ':
            answer += (''.join(new_s[i]) + ' ')
        # 단순한 공백문자라면 answer에 추가한다
        else :
            answer += ' '

    print(answer)
    return answer


s = "  3people unFollowed me  "
# s = "AaaBaa 3People"
# s = "hEllo 1woRld"
solution(s)