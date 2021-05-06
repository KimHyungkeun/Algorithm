# Complete the funnyString function below.
def funnyString(s):
    origin = [] # 본래 순서의 문자열의 아스키코드 리스트
    rev = [] # 역순 문자열의 아스키코드 리스트

    # 각 문자의 아스키코드를 리스트에 넣는다
    for w in s :
        origin.append(ord(w))
        rev.append(ord(w))
    rev.reverse() # reverse함수를 통해 현 리스트 순서를 반대로 한다
    
    # print(origin)
    # print(rev)

    origin_diff = [] # origin 리스트의 각 차를 넣기위한 리스트
    reverse_diff = [] # rev 리스트의 각 차를 넣기위한 리스트
    for i in range(len(origin)-1) :
        origin_diff.append(abs(origin[i]-origin[i+1]))
        reverse_diff.append(abs(rev[i]-rev[i+1]))
    
    # 두 diff 리스트의 결과가 서로 다르면 Not Funny이고, 서로 같다면 Funny이다.
    if origin_diff != reverse_diff :
        return "Not Funny"
    else :
        return "Funny"

    # for i in range(len(origin_diff)) :
    #     if origin_diff[i] != reverse_diff[i] :
    #         return "Not Funny"

    # return "Funny"