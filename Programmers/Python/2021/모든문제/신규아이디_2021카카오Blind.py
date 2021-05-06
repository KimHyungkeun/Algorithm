def solution(new_id):
    answer = ''
    new_id = list(new_id) # 문자 수정을 위해 리스트 타입으로 변환
    
    # 1단계, 2단계
    for i in range(len(new_id)) :
        # 대문자라면 소문자로 치환
        if 'A' <= new_id[i] <= 'Z' :
            new_id[i] = chr(ord(new_id[i]) + 32)
        # 알파벳 소문자, 숫자, '-', '_', '.' 외의 숫자는 전부 제거
        elif 'a' <= new_id[i] <= 'z' or '0' <= new_id[i] <= '9' or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' :
            continue
        else :
            new_id[i] = ''
    
    # 지금까지의 과정을 문자열로 만든 후, 다시 리스트 타입으로 변환
    new_id = ''.join(new_id)
    new_id = list(new_id) 
    
    # 3단계
    for i in range(len(new_id)) :
        # 연속되는 '.'이 발견되는 경우, '.' 하나만 남기고 그 뒤의 연속되는 것은 지워버림
        if new_id[i] == '.' :
            start = i+1
            while start < len(new_id) :
                if new_id[start] == '.' :
                    new_id[start] = ''   
                    start += 1               
                    if start == len(new_id) :
                        break
                else :
                    break

    # 지금까지의 과정을 문자열로 만든 후, 다시 리스트 타입으로 변환            
    new_id = ''.join(new_id)
    new_id = list(new_id)

    # 4단계 : 문자열의 맨 앞뒤에 '.'이 존재한다면 제거한다
    while new_id[0] == '.' or new_id[-1] == '.' :
        if new_id[0] == '.' :
            new_id.pop(0)
        if not new_id :
            break
            
        if new_id[-1] == '.' :
            new_id.pop()
        if not new_id :
            break   


    # 5단계 : 만약 new_id가 빈 문자열이라면 'a'로 초기화
    if len(new_id) == 0 :
        new_id.append('a')    
    
    # 6단계 : 만약 new_id가 15글자를 넘어서면, 맨 뒷글자부터 지워서 15자 이내가 될수있도록 한다
    if len(new_id) >= 16 :
        while len(new_id) > 15 :
            new_id.pop()
        # 맨 뒷자리가 '.' 으로 끝난다면, 맨 뒷자리에 '.'이 아닌 다른 문자가 올때까지 연속으로 제거
        if new_id and new_id[-1] == '.' :
            new_id.pop()


    # 7단계 : new_id가 2이하인 경우, 현재 new_id의 맨 마지막글자를 길이가 3이될때까지 이어붙인다.
    if len(new_id) <= 2 :
        while len(new_id) != 3 :
            new_id.append(new_id[-1])
    
    answer = ''.join(new_id)
    return answer

new_id = "-_.~!@#$%^&*()=+[{]}:?,<>/._-"
solution(new_id)