# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    total = 0 # 총 가격 (s를 넘어선 안된다)
    cnt = 0 # 덧셈이 실행될때마다 카운트 증가
    while True :

        # 현재 가격에서 p만큼 구입했을때, 한도 s를 넘어서면 루프문 종료         
        if total + p > s :
            break
        
        # p가격을 추가하고 카운트를 증가시킴
        total += p
        cnt += 1
        
        # p가격을 d만큼 떨어뜨리되, m 미만으로 떨어질경우엔 m으로 고정
        if p - d < m :
            p = m
        else :
            p -= d
    
    return cnt