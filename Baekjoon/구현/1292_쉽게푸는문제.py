import sys

# 구간 a,b를 설정
a,b = map(int ,sys.stdin.readline().split())

# 숫자는 1은 1번, 2는 2번 이런식으로 증가한다
number = []

cnt = 0
start = 1
while cnt < b :
    # number 리스트에 start를 start수만큼 반복해서 넣는다
    for _ in range(start) :
        number.append(start)
        cnt += 1
        # 만약 b구간을 넘어섰으면 루프문을 탈출한다
        if cnt >= b :
            break

    # 만약 b구간을 넘어섰으면 루프문을 탈출한다
    if cnt >= b :
        break
    
    # start 루프문을 모두 돌고나면 start를 1업 시킨다
    start += 1

print(sum(number[a-1:b]))