def solution(n,a,b):
    answer = 1
    
    # 참가인원 n명에 대해 추가한다
    player = [0] * n
    player[a-1] = a # 참가자 a는 a-1 위치에 있다
    player[b-1] = b # 참가자 b는 b-1 위치에 있다

    # print(player)
    while len(player) != 1 :
        
        # 현재 라운드에서의 a와 b의 위치를 구한다
        pos_a = player.index(a)
        pos_b = player.index(b)

        # 두 선수가 바로 옆짝꿍일때
        if abs(pos_a - pos_b) == 1 :
            if a < b : # 만약 a가 b보다 작고, a의 위치가 나누어떨어지면서 b의 위치가 나누어떨어지지 않으면 둘이 경기에서 만난것이다
                if pos_a % 2 == 0 and pos_b % 2 != 0 :
                    break
            else : # 만약 b가 a보다 작고, b의 위치가 나누어떨어지면서 a의 위치가 나누어떨어지지 않으면 둘이 경기에서 만난것이다
                if pos_b % 2 == 0 and pos_a % 2 != 0 :
                    break
                    
        tmp = []

        # 다음 라운드에 올라갈 사람을 구한다. 단, a와 b는 무조건 이긴다고 가정한다
        for i in range(0,len(player),2) :
            if a in (player[i], player[i+1]) :
                tmp.append(a)
            elif b in (player[i], player[i+1]) :
                tmp.append(b)
            else :
                tmp.append(0)
        
        # 다음 라운드에 올라간 선수명단을 갱신한다
        player = tmp
        # print(player)  
        answer += 1
        

    return answer