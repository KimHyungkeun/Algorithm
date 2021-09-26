def solution(s):
    answer = 0
    
    # 영단어 : 숫자 형태의 딕셔너리
    result = ""
    keyword = {"zero":"0","one":"1", "two":"2", "three":"3", "four":"4","five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    
    tmp = ""
    for w in s :  
        # 해당 글자가 숫자형태의 문자이면 result에 그대로 삽입
        if '0' <= w <= '9' :
            result += w
        # 해당 글자가 알파벳이면 임시 tmp에 추가. 만약 모여있는 글자가 keyword 내에 존재하면, 그 키워드에 맞는 숫자를 리턴
        else :
            tmp += w
            if tmp in keyword :
                # print(tmp)
                result += keyword[tmp]
                tmp = ""
    
    # 최종 결과값은 정수형태
    answer = int(result)
    return answer