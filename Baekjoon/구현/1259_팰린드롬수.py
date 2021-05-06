while True :

    # 문자열 입력
    string = input()
    flag = True

    # 0 입력시에는 종료
    if string == '0' :
        break
    
    # 문자열의 총 길이와, 대칭 기준점이 될 가운데 지점 선택
    length = len(string)
    mid = length // 2

    for i in range(mid) :
        # 만약 대칭구도를 이루지 않으면 팰린드롬이 아님
        if string[i] != string[length-1-i] :
            flag = False
            break
    
    # 팰린드롬이면 yes
    if flag :
        print("yes")
    
    # 아니라면 no를 선택
    else :
        print("no")