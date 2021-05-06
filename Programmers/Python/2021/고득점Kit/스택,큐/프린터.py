from collections import deque
def solution(priorities, location):
    cnt = 0

    prior_idx = [] # 문서 중요도와 문서의 위치를 같이 포함하는 리스트
    for i in range(len(priorities)) :
        prior_idx.append((priorities[i], i)) # 문서와 문서의 위치를 같이 표기

    search = (priorities[location], location) # 찾으려는 문서
    # print(search)
    # print(prior_idx)
    q = deque(prior_idx) # popleft를 위해 해당 리스트를 덱으로 만든다

    maximum = max(q) # 가장 높은 중요도의 문서를 골라낸다
    max_val = maximum[0] # 그중 문서의 중요도만을 따로 저장한다
    # print(max_val)
    
    while q :
        
        while q[0][0] != max_val :
            q.append(q.popleft()) # 현재 프린터 대기열중 최고 중요도를 가진 문서를 찾을때까지 순환반복
            # print(q)
        
        if search == q[0] : # 만약 해당 문서가 사용자가 원하는 문서라면 루프문 탈출
            cnt += 1
            break
        
        else :
            q.popleft() # 아니라면 일단 해당문서는 출력을 완료한다
            cnt += 1
            maximum = max(q)
            max_val = maximum[0] # 그리고 남은 대기문서중에 그다음으로 중요도가 높은 문서를 설정한다
            # print("max : ", max_val)
            

    print(cnt)
    return cnt

# priorities = [2,1,3,2]
# location = 2

priorities = [1,1,9,1,1,1]
location = 0
solution(priorities, location)