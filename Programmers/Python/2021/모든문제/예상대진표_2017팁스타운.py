def solution(n,a,b):
    rounds = 1 # 1라운드부터 시작
    player = [[i, i+1] for i in range(1,n+1,2)] # [1,2], [3,4], ... ,[n-1,n] 순으로 대진표가 짜여진다
    
    # 원활한 계산을 위해, 원하는 플레이어가 a,b 순서대로 오름차순이 되도록 한다
    if a > b :
        a,b = b,a
    
    while len(player) != 1 :
        # 만약 a,b 두선수가 만나게되면 루프문을 탈출한다
        if [a,b] in player :
            break
            
        tmp = []
        for i in range(len(player)) :
            # 만약 해당 대진표에 a,b 선수 둘다 없으면, 아무나 다음 라운드로 진출시킨다
            if a not in player[i] and b not in player[i] :
                tmp.append(player[0])
            # 만약 a선수가 있다면, a선수를 무조건 진출시킨다
            elif a in player[i] :
                tmp.append(a)
            # 만약 b선수가 있다면, b선수를 무조건 진출시킨다
            else :
                tmp.append(b)
        
        # 올라간 라운드에 대한 대진표를 재구성한다
        player = []
        for i in range(0, len(tmp),2) :
            player.append([tmp[i], tmp[i+1]])
        
        # 새 대진표가 짜여졌으므로 라운드수를 올린다
        rounds += 1
                   
    return rounds