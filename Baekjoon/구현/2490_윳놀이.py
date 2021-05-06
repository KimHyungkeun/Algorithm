import sys

for _ in range(3):
    yoot = list(map(int, sys.stdin.readline().split()))

    # 모두 앞면이면 모
    if yoot.count(0) == 0 :
        print("E")
    
    # 뒷면이 하나이면 도
    elif yoot.count(0) == 1 :
        print("A")
    
    # 뒷면이 둘이면 개
    elif yoot.count(0) == 2 :
        print("B")
    
    # 뒷면이 셋이면 걸
    elif yoot.count(0) == 3 :
        print("C")

    # 뒷면이 넷이면 윷
    elif yoot.count(0) == 4 :
        print("D")