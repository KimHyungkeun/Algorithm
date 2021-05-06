import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    h,w,n = map(int, sys.stdin.readline().split())

    # 호실은 X01호부터 시작한다
    start_room = 1 # 방번호는 1번부터 시작한다
    idx_n = n - 1 # 나머지연산을 위해, 0부터 세어서 카운트한다. 즉, n-1번째 라는 뜻

    floor = (idx_n % h) + 1# w호에 대해 꼭대기 층까지 올라갔을 경우, 그다음 방배정은 다시 맨 아래층부터 시작하고 w+1호부터 손님을 배정
    order_no = start_room + (idx_n // h) # w호가 하나 증가했으므로 w+1호가 된다

    str_floor = str(floor)
    if order_no < 10 : # 방번호가 10 미만이면, 숫자앞에 '0'을 붙인다
        str_order_no = '0'+str(order_no)
    
    else : 
        str_order_no = str(order_no)
    
    # 최종 방번호
    room_no = str_floor + str_order_no
    print(room_no)
    
    
    



    



