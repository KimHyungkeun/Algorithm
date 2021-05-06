from collections import deque
# Complete the rotLeft function below.
def rotLeft(a, d): # a는 1 ~ n 까지의 배열, d는 로테이션 횟수
    
    array = deque(a) # 해당 배열을 덱으로 구성한다
    
    # 총 d번, 맨 앞쪽의 원소를 맨 뒷쪽순서로 보낸다.
    while d != 0 :
        array.append(array.popleft())
        d -= 1
    
    # d번 로테이션을 돌고 난 후의 리스트를 리턴한다
    result = list(array)
    return result