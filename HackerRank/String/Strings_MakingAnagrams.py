# Complete the makeAnagram function below.
def makeAnagram(a, b):

    cnt = 0 # 아나그램 생성을 위해 제거해야할 철자 갯수
    a_dict = {} # a 문자열에 있는 알파벳 갯수를 담기위한 dict
    b_dict = {} # b 문자열에 있는 알파벳 갯수를 담기위한 dict
    
    # a 문자열에 있는 철자 종류와 갯수 카운팅
    for w in a :
        if w in a_dict :
            a_dict[w] += 1
        else :
            a_dict[w] = 1
    
    # b 문자열에 있는 철자 종류와 갯수 카운팅
    for w in b :
        if w in b_dict :
            b_dict[w] += 1
        else :
            b_dict[w] = 1
    
    # a,b 문자열에서 공통적으로 발견되는 철자의 종류를 추출하고, a와 b의 공통철자중 출현횟수가 적은것을 intersection에 누적시킨다
    intersection = 0
    for key,val in a_dict.items() :
        if key in b_dict :
            intersection += min(a_dict[key], b_dict[key])
    # print(intersection)
    
    # 각 a와 b의 길이에서의 공통출현철자의 갯수를 제외하면, 그 나머지 철자들이 아나그램 생성을 위해 제거되어야할 철자의 갯수가 된다
    cnt = (len(a) - intersection) + (len(b) - intersection)
    
    return cnt