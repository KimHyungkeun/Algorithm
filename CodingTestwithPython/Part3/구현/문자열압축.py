def solution(s):
   
    length = len(s) # 문자열 총 길이
    min_length = 1000 # 최대 가능한 문자열 길이가 1000이므로 이를 최소값을 설정
    
    
    for i in range(1, length+1) : # 처음부터 i개씩 잘라서 확인해본다

        start = 0 # 처음 
        end = i # i번째 까지

        result = "" # 최종 문자열
        tmp = "" # i길이 만큼 잘랐을때의 부분 문자열
        combo = 0
        
        # print(start, end)
        while start <= length-1 :

            if tmp == "" : # tmp가 비어있다면 초반의 부분 문자열 입력
                tmp = s[start:end]
       
            if tmp == s[start:end] : # 현재 잘랐을때의 부분문자열이 tmp와 같다면 콤보수 증가
                combo += 1
                # print(tmp)
            
            else :
                if combo <= 1 : # 만약 1이하 콤보이면 문자열 자체만 첨가
                    result += tmp
                else :
                    result += (str(combo) + tmp) # 만약 2 이상 콤보이면 콤보수 + 문자열 형태로 result에 추가
                tmp = s[start:end]
                # print(tmp)
                combo = 1

             # i길이 만큼 start와 end의 위치를 옮김
            start += i
            end += i
        
        # 못다한 길이에 대해서 한번 더 확인
        if combo <= 1 :
                result += tmp
        else :
            result += (str(combo) + tmp) 
        
        # print(result)

        # 더 짧은 형태의 문자열이 있다면, 그 문자열의 길이를 구한다
        if len(result) < min_length :
            min_length = len(result)


    # print(min_length)
    return min_length

# s = "aabbacccd"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
# s = "aaabbbccdd"
solution(s)