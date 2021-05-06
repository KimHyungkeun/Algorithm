import heapq
def solution(operations):
    answer = []
    q = [] # 큐

    for cmd in operations :
        if cmd.split(" ")[0] == 'I' : # I일때는 값 삽입
            num = int(cmd.split(" ")[1])
            q.append(num)
        
        else : 
            if q :  
                q.sort() # 오름차순 정렬
                # 1일때는 최댓값을 제외
                if cmd.split(" ")[1] == "1" :
                   q.pop()
                # -1일때는 최소값을 제외
                else :
                    q.pop(0)
    
    # 큐가 비었다면 [0,0] 출력
    if not q :
        answer = [0,0]
    
    # 정상경우에는 최댓값, 최소값 출력
    else :
        answer = (max(q), min(q))
    
    print(answer)
    return answer


operations = ["I 16","D 1"]
solution(operations)