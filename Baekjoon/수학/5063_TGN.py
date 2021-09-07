import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    r,e,c = map(int,sys.stdin.readline().split())

    # 광고하지 않았을때 보다, 광고한 수익이 더 높을때
    if r < e - c :
        print("advertise")
    
    # 광고하지 않은것과, 광고한 수익이 별반 차이 없을때
    elif r == e - c :
        print("does not matter")
    
    # 광고했을 때 수익으로 더 손해보는 경우
    else :
        print("do not advertise")