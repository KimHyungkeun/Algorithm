def matchingStrings(strings, queries):
    # Write your code here
    result = [] # 해당 질의에 대한 결과값을 담는 배열

    dict_str = {} # string 종류에 따른 갯수 딕셔너리

    # strings에 대한 등장 빈도수를 담은 딕셔너리를 설정한다
    for s in strings :
        if s not in dict_str :
            dict_str[s] = 1
        else :
            dict_str[s] += 1
    
    # 쿼리문을 넣어서, 해당 쿼리(문자열 등장 횟수)에 대한 결과값을 result에 담는다
    for q in queries :
        if q not in dict_str :
            result.append(0) # 아예 등장하지 않으면 0을 추가
        else :
            result.append(dict_str[q]) # 그 외의 경우라면, 해당 문자열의 등장횟수 추가
    
    return result