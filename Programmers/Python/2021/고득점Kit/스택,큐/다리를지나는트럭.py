def summary(argu) : # trucks 배열에서 해당 트럭의 무게만을 모두 더하기위해 만든 덧셈 함수
    summary = 0
    for i in argu :
        summary += i[0]
    return summary

def solution(bridge_length, weight, truck_weights):
    sec = 0
    trucks = []

    for t in truck_weights :
        trucks.append([t,0]) # 해당 트럭의 무게와 지나간 길이(초)를 담기위해 포맷을 변경

    end_truck = [] # 도착한 트럭
    cross_truck = [] # 지나가는 중인 트럭
    
    while cross_truck or trucks :
        if not cross_truck :
            if weight < trucks[0][0] : # 해당 트럭이 지탱가능한 무게를 넘어서면 안된다
                break
            else :
                trucks[0][1] += 1 # 대기열 트럭에서 빠져나와 다리를 건너기 시작한다
                cross_truck.append(trucks.pop(0))
                

        else :
                  
            for t in cross_truck : # 트럭은 1초당 1만큼 간다
                t[1] += 1

            if cross_truck[0][1] > bridge_length : # 만약 해당 트럭이 다리를 다 지나면 end_truck에 넣는다
                cross_truck.pop(0)
            
            if trucks and summary(cross_truck) + trucks[0][0] <= weight : # 다리에 새로운 트럭이 들어올 수 있는 경우에는 트럭을 다리에 투입시킨다
                trucks[0][1] += 1
                cross_truck.append(trucks.pop(0))
            
            

        # print("end_truck : ", end_truck, "cross_truck : ", cross_truck)    
        sec += 1

    print(sec)
    return sec

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 1100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)

