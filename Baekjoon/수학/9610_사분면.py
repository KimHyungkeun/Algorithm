import sys

n = int(sys.stdin.readline())
coordinate = {"Q1":0, "Q2":0, "Q3":0, "Q4":0, "AXIS":0}

for _ in range(n) :
    x, y = map(int,sys.stdin.readline().split())

    # 좌표가 축에 존재할때
    if x == 0 or y == 0 :
        coordinate["AXIS"] += 1
    
    # 1사분면에 위치
    elif x > 0 and y > 0 :
        coordinate["Q1"] += 1
    
    # 2사분면에 위치
    elif x < 0 and y > 0 :
        coordinate["Q2"] += 1
    
    # 3사분면에 위치
    elif x < 0 and y < 0 :
        coordinate["Q3"] += 1
    
    # 4사분면에 위치
    else :
        coordinate["Q4"] += 1
    
print("Q1:", coordinate["Q1"])
print("Q2:", coordinate["Q2"])
print("Q3:", coordinate["Q3"])
print("Q4:", coordinate["Q4"])
print("AXIS:", coordinate["AXIS"])