from collections import deque

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    depth = 0 # 깊이 설정
    queue = deque()  # 덱 설정
    queue.append(0) # 0번째로부터 시작한다
    length = len(queue) # 해당 depth에서의 덱 길이
    
    while queue :
        idx = queue.popleft() # 덱에서 인덱스번호를 하나 뽑는다
        length -= 1 # 덱에서 하나 뽑았기때문에 길이가 감소한다
        if c[idx] == 0 : # 해당 인덱스 번째가 안전구역이라면

            # c 영역 내에서의, idx+1번째, idx+2번째 구름을 불러온다
            if idx+1 < len(c) :
                queue.append(idx+1)
            if idx+2 < len(c) :
                queue.append(idx+2)
        # print(queue)
        
        if length == 0 : # 만약 해당 depth에서의 비교가 모두 끝나면
            length = len(queue) # 새로운 depth에서의 큐 길이로 갱신하고, depth도 한단계 더 들어간다
            depth += 1 
            if len(c)-1 in queue : # 만약 해당 depth에서 목적지에 해당하는 경우가 존재하면 루프문을 탈출한다
                break
    
    return depth