import sys

t = int(sys.stdin.readline())


for _ in range(t) :
    total_y = 0
    total_k = 0
    for i in range(9) :
        y, k = map(int,sys.stdin.readline().split())
        total_y += y
        total_k += k
    
    # 연세대가 이겼으면 Yonsei 출력
    if total_y > total_k :
        print("Yonsei")
    
    # 고려대가 이겼으면 Korea 출력
    elif total_y < total_k :
        print("Korea")
    
    # 비겼다면 Draw 출력
    else :
        print("Draw")
