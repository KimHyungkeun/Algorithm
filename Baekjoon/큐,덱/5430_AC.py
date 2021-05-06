from collections import deque
import sys

n = int(sys.stdin.readline()) # 횟수 입력

for _ in range(n) :
    cmd = input() # 작동시킬 함수를 입력
    num = int(input()) # 배열 갯수 정함
    string = input() # [,,] 형태로 배열입력
    string = string[1:-1] # [] 기호를 제외한 실질적인 부분만  슬라이싱
    is_reverse = -1 # 뒤집기에 따른 플래그
    flag_D = False # 배열 사이즈가 0인 상태에 대해서, 버리기를 시전할 경우 에러를 띄우기 위한 플래그

    # print(string)
    arr_str = string.split(",") # ,를 기준으로 숫자들만 배열에 넣음
    arr = deque(arr_str) # 원활한 작업을 위해 덱을 설정


    for c in cmd :
        # print(arr)
        if c == 'R' :
            is_reverse *= -1 # R은 뒤집기

        elif c == 'D' :     
            if not arr or arr[0] == '': # D는 꺼내기, ''로 조건을 세운 이유는 문자열 입력이기에, 아무것도 입력하지 않은것을 ''로 인식하기 때문
                flag_D = True
                break

            else :
                if is_reverse == 1 :
                    arr.pop() # 실제로 뒤집지는 않고, 맨 뒷쪽의 숫자부터 차례대로 제거
                else :
                    arr.popleft() # 원래 순서의 경우, 맨 앞부터 차례대로 제거

    # print(arr ,flag_D)

    if (not arr or arr[0] == '') and flag_D:
        print("error") # 만약 배열이 비었는데, D함수를 쓰면 에러를 출력

    else : 
        if is_reverse == 1 : # 만약 뒤집기가 활성화된 상태라면
            arr = list(arr)
            arr.reverse() # 실제 남은 배열의 순서를 거꾸로 뒤집고 출력
            print('['+ ','.join(map(str, arr)) + ']')

        else : # 뒤집기가 비활성화이면, 현재 순서 그대로 출력
            print('['+ ','.join(map(str, arr)) + ']')

