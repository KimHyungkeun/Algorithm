def solution(msg):
    answer = []
    index = {chr(i+64):i for i in range(1, 27)} # A ~ Z 까지 각각 1 ~ 26까지의 고유번호를 부여한다
    
    cur = 26
    i = 0
    while i < len(msg) :
        cnt = 0
        for j in range(i, len(msg)) :
            # 만약 해당 단어가 딕셔너리 내에 있으면, 그 다음 문자까지 합한 단어가 있는지도 확인한다
            if msg[i:j+1] in index :          
                cnt += 1
            else :
                # 만약 해당 단어가 처음 나오는 단어라면, 딕셔너리에 새로 등록한다
                answer.append(index[msg[i:j]]) # 딕셔너리에 처음 등장하는 단어가 나오기 바로 이전단계에 대해서는, 해당 단어의 고유번호를 출력한다
                cur += 1
                index[msg[i:j+1]] = cur # 고유번호는 새로 추가될수록 1씩 증가하는 형태이다
                break
        
        if i+cnt < len(msg) :
            i += cnt # 새로 등장한 단어의 문자열 길이만큼, 문자열 검사위치를 이동 시킨다 
        else :
            break
    
    answer.append(index[msg[i:j+1]]) # 마저 계산하지 못한 단어에 대해서도 확인

    return answer