import sys

num = int(sys.stdin.readline())

for _ in range(num) :
    k = int(sys.stdin.readline()) # k층, 0층 ~ k층
    n = int(sys.stdin.readline()) # n호, 1호 ~ n호

    room = [] # 호실별 인원
    for i in range(n) :
        room.append(i+1) # i호에는 i명이 산다

    # k층의 n호에 살려면 자신의 바로 아래(k-1)층의 1호부터 n호까지 사람들의 수의 합만큼 데려와 살아야 한다
    new_room = [0]*n # i개의 호실이 존재

    if k == 0 : # 0층은 i호실에 i명이 산다.
        print(room[n-1])
    
    else :
        for _ in range(k) :
            summary = 0
            for j in range(n) : # i층 1호 인원 = i-1층 1호인원, i층 2호 인원 = i-1층 1호인원 + i-1층 2호 인원 규칙대로 인우너 배정 
                summary += room[j] 
                new_room[j] = summary
            room = new_room

        print(new_room[n-1]) # 호실은 1부터 세지만, 인덱스는 0부터 세므로 -1을 해준다.

