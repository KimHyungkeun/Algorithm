import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    d = ((x1-x2)**2 + (y1-y2)**2)**0.5

    # 1. 두 원이 서로 겹칠때
    if abs(r2-r1) < d < abs(r1+r2) :
        print(2)
    
    # 2. 두 원이 한 점에서 만날때(외접)
    elif r1 + r2 == d :
        print(1)
    
    # 3. 두 원이 한 점에서 만날때(내접), d = 0 인 경우는 동심원이기에 조건에서 제외
    elif abs(r2-r1) == d and d != 0 :
        print(1)
    
    # 4. 두 원이 서로 멀리 떨어진 경우
    elif r1 + r2 < d :
        print(0)

    # 5. 작은 원이 큰 원 안에 있으면서 서로 만나지 않을 때
    elif abs(r2-r1) > d  :
        print(0)
    
    # 6. 동심원일때
    elif d == 0 :
        if r1 == r2 : # 똑같은 크기의 원이라면, 무수히 많이 만남
            print(-1)
        else : 
            print(0) 


