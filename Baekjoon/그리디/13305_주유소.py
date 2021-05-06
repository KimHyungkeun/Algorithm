import sys

n = int(sys.stdin.readline())

# 도시간의 거리
distance = list(map(int, sys.stdin.readline().split()))
# 각 도시별 주유 가격
cost = list(map(int, sys.stdin.readline().split()))

i = 0
length = len(distance) # 거리들을 배열로 표현
current = 0 # 현 도시의 주유가격을 임시저장
summary = 0 # 누적된 가격

# 목적지까지의 일정
while i != length :
    
    # 만약 현재 도시가격이 다음 도시가격보다 비쌀 경우
    # (다음 도시까지의 거리) X (현재 도시에서의 주유 가격)
    if cost[i] >= cost[i+1] :
       summary += distance[i] * cost[i]
       i += 1
    
    # 다음 도시가격이 현재 도시가격보다 비쌀 경우
    # (현재 도시 주유가격보다 작거나 같은 도시까지의 총 거리) X (현재 도시에서의 주유 가격)
    else :
        current = cost[i]
        add = 1 
        count = 0
        summary += distance[i] * current

        # 현재도시보다 주유가격이 싼 도시가 나올때 까지, 현재 도시에서 주유를 지속함
        while current < cost[i+add] :
            count += distance[i+add] * current
            add += 1
            if i+add == length :
                break
        
        # 이동하는 동안 누적된 주유가격을 저장
        summary += count
        i += add

    

print(summary)    
    
    

            

