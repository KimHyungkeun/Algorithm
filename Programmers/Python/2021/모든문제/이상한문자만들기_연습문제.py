def solution(s):
    answer = ''
    arr = s.split(" ",-1) # 해당 문자열을 공백기준으로 나누고, 후반에 있을 공백은 없는것 처리한다
    
    new_arr = []
    for i in range(len(arr)) :
        # 문자열 수정을 위해, 해당 arr[i]를 리스트 타입으로 바꾼다
        tmp = list(arr[i])  
        for j in range(len(arr[i])) :                             
            # 짝수번째 인덱스일때는 대문자로 바꿈   
            if j % 2 == 0 :
                if 'a' <= tmp[j] <= 'z' :
                    tmp[j] = chr(ord(tmp[j]) - 32)
            # 홀수번째 인덱스일때는 소문자로 바꿈
            else :
                if 'A' <= arr[i][j] <= 'Z' :
                    tmp[j] = chr(ord(tmp[j]) + 32)
        # 수정이 완료된 리스트를 문자열로 편입 후, new_arr에  추가
        new_arr.append(''.join(tmp))
    
    for i in range(len(new_arr)) :
        # 마지막 인덱스번째일때는 문자열 자체만 추가
        if i == len(new_arr) - 1 :
            answer += new_arr[i]
        # 그 이전 인덱스번째일때는 문자열에 공백까지 후반에 추가
        else :
            answer += (new_arr[i] + ' ')

    # 값 리턴
    return answer

s = "aBcDe"
solution(s)

# 참고 : https://programmers.co.kr/questions/16105, "hello world   "와 같이 뒷쪽의 공백문자 있을경우를 생각 못함