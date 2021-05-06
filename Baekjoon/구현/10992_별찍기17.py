import sys


# 채워짐 없이 변만으로만 구성된 삼각형 찍기

n = int(sys.stdin.readline())
total = 2*n -1 # n이 1,2,3,4라면 total은 1,3,5,7이다

# n이 1이나 2일 경우에는 다음과 같이 표기
if n == 1 : 
    print("*")

elif n == 2 :
    print(" *")
    print("***")

# n이 3 이상일때
else :
    mid = total // 2 # 먼저 total의 중간값을 구한다
    for i in range(1,n+1) :
        
        if mid == 0 : # 만약 마지막 순서일경우에는 total 크기만큼 모든 별을 출력한다
            for _ in range(total) :
                print("*",end='')
        
        else :
            for j in range(mid) : # 중간지점 이전까지는 공백을 출력
                print(" ",end='')
            
            if i >= 2 : # 2번째 차례 이상인 경우
                print("*",end='') # mid에는 별을 찍고
                blank = 2*(i-1) - 1 # i번째인 경우 2*(i-1) - 1 만큼의 갯수만큼 공백을 설정한다
                for _ in range(blank) :
                    print(" ",end='') # 공백을 출력한후, 마지막은 별을 찍는다
                print("*")

            else : # 만약 이번차례가 첫번째 차례라면 별 1개로 마무리 짓는다
                print("*")
        
        mid -= 1 # mid가 0이될때까지 1씩 줄어든다
            


