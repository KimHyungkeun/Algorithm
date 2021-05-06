import sys

# 배열을 입력받는다. 연산의 최종결과는 answer 배열처럼 나와야 한다 
array = list(map(int, sys.stdin.readline().split()))
answer = sorted(array)

while True :

    # 1. 첫번째가 두번째 수보다 크다면 서로 맞바꾼다. 먄약, 오름차순정렬이 완료되면 루프문을 종료한다.
    if array[0] > array[1] :
        array[0],array[1] = array[1], array[0]
        print(*array)
        if array == answer :
            break
    
    # 2. 두번째가 세번째 수보다 크다면 서로 맞바꾼다. 먄약, 오름차순정렬이 완료되면 루프문을 종료한다.
    if array[1] > array[2] :
        array[1],array[2] = array[2], array[1]
        print(*array)
        if array == answer :
            break

    # 3. 세번째가 네번째 수보다 크다면 서로 맞바꾼다. 먄약, 오름차순정렬이 완료되면 루프문을 종료한다.        
    if array[2] > array[3] :
        array[2],array[3] = array[3], array[2]
        print(*array)
        if array == answer :
            break
    
    # 4. 네번째가 다섯번째 수보다 크다면 서로 맞바꾼다. 먄약, 오름차순정렬이 완료되면 루프문을 종료한다.
    if array[3] > array[4] :
        array[3],array[4] = array[4], array[3]
        print(*array)
        if array == answer :
            break
        
          
# print(array)
# print(answer)