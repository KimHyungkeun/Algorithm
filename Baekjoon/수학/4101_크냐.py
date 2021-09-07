import sys

while True :
    # a가 b보다 크면 Yes를 출력하고 아니면 No를 출력
    # a,b가 모두 0이면 종료
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 :
        break

    elif a > b :
        print("Yes")
    
    else :
        print("No")