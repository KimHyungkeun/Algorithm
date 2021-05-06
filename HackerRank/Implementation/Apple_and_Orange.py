# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    # s와 t 사이에 존재하는 사과와 오렌지의 갯수를 각각 구하는 문제

    cnt_apple = 0 # 사과 갯수
    cnt_oranges = 0 # 오렌지 갯수
    
    for i in range(len(apples)) :
        # 사과나무 a에서 사과 apple[i]까지의 거리 구함
        apples[i] += a
        # 만약 s와 t 사이에 있다면 카운트를 증가
        if s <= apples[i] <= t :
            cnt_apple += 1
    
    for i in range(len(oranges)) :
        # 오렌지나무 b에서 오렌지 orange[i]까지의 거리 구함
        oranges[i] += b
        # 만약 s와 t 사이에 있다면 카운트를 증가
        if s <= oranges[i] <= t :
            cnt_oranges += 1
    
    # 각 사과와 오렌지 갯수 출력
    print(cnt_apple)
    print(cnt_oranges)