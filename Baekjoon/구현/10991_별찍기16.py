import sys

# 빈칸까지 모두 포함하면, 출력해야할 범위는 n * (2*n - 1) 이다
n = int(sys.stdin.readline())
m = 2*n-1 

# 해당 row의 중간지점의 인덱스
mid = m // 2 


for i in range(n) :
    k = mid-i # 해당 인덱스 전까지는 모두 공백을 채우기 위함
    tmp = i+1 # 해당 row에서 찍어야할 별 갯수를 제한
    flag = True # 별일지 공백일지 판단하기 위한 플래그
    for j in range(m) :
        # 해당 row가 시작되기 전까지는 mid-i번째 칸까지 모두 공백처리한다
        if j < k :
            print(" ",end='')
        else :
            if tmp != 0 and flag:
                print("*",end='') # 만약 처리해야할 별이 남아있다면 출력한다
                flag = False
                tmp -= 1
                if tmp == 0 : # 해당 row에서 허락된 출력갯수를 모두 소모하면 다음 row로 넘어간다
                    print()
                    break

            elif not flag :
                print(" ",end='') # 별을 찍을 차례가 아니면 공백을 출력한다
                flag = True
            
