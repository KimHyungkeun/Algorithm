def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    # 가능한 경우를 담는 리스트
    able = set([])

    for k in keyboards :
        for d in drives :
            # 만약 키보드와 USB드라이브의 가격이 b 이하라면, 리스트에 담는다
            if k+d <= b :
                able.add(k+d)
    
    # 가격 b 이하로 살수있는것이 하나도 없다면 -1을 리턴하고, 그렇지 않으면 b와 가까운 가장 큰 가격을 리턴한다
    if not able :
        return -1
    else :
        return max(able)